import os
from pathlib import Path

def write_file(working_directory, file_path, content):
    try:
        permitido = Path(os.path.abspath(Path(working_directory)))
        if file_path.startswith(".."):
            file = permitido.parent
        else:
            file = Path(os.path.join(permitido, Path(file_path)))
        if not file.is_relative_to(permitido):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file.parent):
            os.makedirs(file, mode=0o777, exist_ok=False)


        with open(file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"    