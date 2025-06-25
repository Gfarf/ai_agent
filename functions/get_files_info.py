import os
from pathlib import Path
from google.genai import types

def get_files_info(working_directory, directory=None):
    try:
        permitido = Path(os.path.abspath(Path(working_directory)))
        if directory.startswith(".."):
            caminho = permitido.parent
        else:
            caminho = Path(os.path.join(permitido, Path(directory)))
        if not caminho.is_relative_to(permitido):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(caminho):
            return f'Error: "{directory}" is not a directory'
        
        list = os.listdir(caminho)
        r_string = ""
        for file in list:
            fullfile = Path(os.path.join(caminho, Path(file)))
            size = os.path.getsize(fullfile)
            direc = not os.path.isfile(fullfile)
            r_string += f"- {file}: file_size={size} bytes, is_dir={direc}\n"
        return r_string



    except Exception as e:
        return f"Error:{str(e)}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    