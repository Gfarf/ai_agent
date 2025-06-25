import os
from pathlib import Path

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    file_content_string = ""
    try:
        permitido = Path(os.path.abspath(Path(working_directory)))
        if file_path.startswith(".."):
            file = permitido.parent
        else:
            file = Path(os.path.join(permitido, Path(file_path)))
        if not file.is_relative_to(permitido):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        
    except Exception as e:
        file_content_string = f"Error: {e}"
    
    return file_content_string
    