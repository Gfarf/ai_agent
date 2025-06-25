import os
from pathlib import Path
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write the content to the defined file, creating it if it does not exist, overwriting if it does exist, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path relative to the working directory to find the file to write on.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="What shall be written in the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)