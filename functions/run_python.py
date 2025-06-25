import os
from pathlib import Path
import subprocess

def run_python_file(working_directory, file_path, args=None):
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
        commands = ["python3",file]
        if args:
            commands.extend(args)
        result = subprocess.run(commands, capture_output=True, text=True, timeout=30)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"    