from google.genai import types
from functions.get_files_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file
from config import working_directory

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    functions_calls = {"get_file_content": get_file_content, "get_files_info": get_files_info, "run_python_file": run_python_file, "write_file": write_file}
    if functions_calls.get(function_name, False) == False:
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )
    executable = functions_calls[function_name]
    result = executable(working_directory, **function_args)
    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": result},
                )
            ],
        )
