import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


def main(*args, **kwargs):
    arg_list = sys.argv
    if len(arg_list) < 2:
        print("must include a prompt in the command line")
        exit(code=1)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    '''
    if len(sys.argv) > 1:
        print("Command-line arguments:")
        for i, arg in enumerate(sys.argv[1:]):
            print(f"  Argument {i+1}: {arg}")
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")

    n_args = parser.parse_args()
    '''

    user_prompt = arg_list[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
    if len(arg_list) > 2:
        if arg_list[2] == "--verbose":
            print(f"User prompt: {user_prompt}")
            print(response)
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response) 



if __name__ == "__main__":
    main()