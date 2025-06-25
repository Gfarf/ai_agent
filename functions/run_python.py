import os
from pathlib import Path
import subprocess

def run_python_file(working_directory, file_path):
    try:
        permitido = Path(os.path.abspath(Path(working_directory)))
        if file_path.startswith(".."):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        file = Path(os.path.join(permitido, Path(file_path)))
        if not file.is_relative_to(permitido):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'


        comp_process = subprocess.run(["python3",file], capture_output=True, timeout=30)
#        print(comp_process)
#        print(f'STDOUT: {comp_process.stdout}')
#        print(f'STDERR: {comp_process.stderr}')
        if comp_process.stdout == '' and comp_process.stderr == '':
            return "No output produced."
        result = 'STDOUT: ' + str(comp_process.stdout, 'utf-8') + '\nSTDERR: ' + str(comp_process.stderr, 'utf-8')
        if comp_process.returncode != 0:
            result += f"Process exited with code {comp_process.returncode}"

        return result

    except Exception as e:
        return f"Error: executing Python file: {e}"    