import os
import sys
import subprocess
import json

def discover_venv_executable():
    if os.name == "nt":
        return os.path.join("venv", "Scripts", "python.exe")
    return os.path.join("venv", "bin", "python")

def validate_environment(executable_path):
    if not os.path.exists(executable_path):
        print("Erro Critico [BIA CLI]: O ambiente virtual 'venv' nao foi encontrado.")
        print("Solucao: Execute 'python -m venv venv' na raiz do projeto.\n")
        sys.exit(1)

def execute_shell_session():
    print("=== BIA: Abrindo terminal isolado (Digite 'deactivate' para sair) ===\n")
    if os.name == "nt":
        subprocess.run(["powershell", "-NoExit", "-Command", ".\\venv\\Scripts\\Activate.ps1"])
    else:
        subprocess.run(["bash", "--rcfile", "venv/bin/activate"])

def execute_pipeline(arguments):
    if not arguments:
        print("\nErro [BIA CLI]: O comando 'run' exige o arquivo da tarefa.")
        print("Exemplo: python bia.py run bia_task_settings.json\n")
        sys.exit(1)
    isolated_python = discover_venv_executable()
    execution_command = [isolated_python, "main_orchestrator.py"] + arguments
    try:
        subprocess.run(execution_command, check=True)
    except subprocess.CalledProcessError as error:
        print(f"Erro [BIA CLI]: Falha na execucao da tarefa (Codigo {error.returncode})\n")
        sys.exit(error.returncode)

def execute_custom_script(script_command):
    print(f"=== BIA: Executando Comando Customizado ===")
    print(f"\nComando: {script_command}\n")
    try:
        subprocess.run(script_command, shell=True, check=True)
    except subprocess.CalledProcessError as error:
        print(f"Erro [BIA CLI]: O script externo falhou (Codigo {error.returncode})\n")
        sys.exit(error.returncode)

def get_internal_registry(arguments):
    return {
        "shell": execute_shell_session, 
        "run": lambda: execute_pipeline(arguments)
    }

def get_external_registry():
    settings_path = os.path.join("config", "settings.json")
    if not os.path.exists(settings_path):
        return {}
    try:
        with open(settings_path, "r", encoding="utf-8") as file:
            config_data = json.load(file)
            return config_data.get("scripts",{})
    except json.JSONDecodeError:
        print("Aviso [BIA CLI]: O arquivo settings.json esta corrompido.\n")
        return {}

def route_cli_command(command, arguments):
    isolated_python = discover_venv_executable()
    validate_environment(isolated_python)
    internal_registry = get_internal_registry(arguments)
    external_registry = get_external_registry()
    if command in internal_registry:
        internal_registry[command]()
    elif command in external_registry:
        execute_custom_script(external_registry[command])
    else:
        print(f"\nErro [BIA CLI]: Comando \"{command}\" nao reconhecido.")
        print(f"\nComandos nativos: \n=> {"\n=> ".join(internal_registry.keys())}")
        if external_registry:
            print(f"\nComandos customizados: \n=> {"\n=> ".join(external_registry.keys())}")
        print("")
        sys.exit(1)

if __name__ == "__main__":
    cli_arguments = sys.argv[1:]
    if not cli_arguments:
        internal_registry = get_internal_registry([])
        external_registry = get_external_registry()
        print("=== BIA CLI (Motor Preditivo ETL) ===")
        print("\nUso: \n=> python bia.py [comando] [argumentos]")
        print(f"\nComandos nativos: \n=> {"\n=> ".join(internal_registry.keys())}")
        if external_registry:
            print(f"\nComandos customizados: \n=> {"\n=> ".join(external_registry.keys())}")
        print("")
        sys.exit(1)
    main_command = cli_arguments[0]
    extra_arguments = cli_arguments[1:]
    route_cli_command(main_command, extra_arguments)