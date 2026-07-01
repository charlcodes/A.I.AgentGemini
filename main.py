import os
from pyclbr import Function
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse as ap 
from config import system_prompt
from functions.call_function import available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("API key was not fetched, check variables.")

client = genai.Client(api_key=api_key)



def main():
    parser = ap.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # trying to keep chat list resubmit
    messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
]

    #user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    #print("Hello from ai-agent!")
    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents= messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
)
    if response.usage_metadata:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
    else:
        raise RuntimeError("Meta data is None")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")
        message = f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}"
        print(message)
    
    if response.function_calls is not None:
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
