import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from fs_tools import (
    read_file,
    list_files,
    write_file,
    search_in_file
)

from tool_definitions import tools


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


available_functions = {
    "read_file": read_file,
    "list_files": list_files,
    "write_file": write_file,
    "search_in_file": search_in_file
}


def main():

    user_prompt = input("You: ")

    messages = [
        {
            "role": "system",
            "content": """
You are a file assistant for a resume management system.

Resume files are stored in:
data/resumes/

Generated files must be stored in:
output/

Rules:

1. If the user gives only a resume filename, use data/resumes/<filename>.

2. If the user asks to read all resumes:
   first use list_files on data/resumes.

3. If the user asks to find a keyword across resumes:
   first use list_files on data/resumes,
   then use search_in_file on the relevant files.

4. If the user asks to create a summary:
   first read the resume,
   create a concise summary,
   then use write_file to save it inside output/.

5. Always use the provided tools to access files.
   Never invent file contents.

6. Continue using tools until the user's request is completely fulfilled.
"""
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    while True:

        response = client.chat.completions.create(
            model="openai/gpt-4.1-mini",
            messages=messages,
            tools=tools,
            max_tokens=1000
        )

        message = response.choices[0].message

        messages.append(message)

        if not message.tool_calls:
            print("\nAssistant:")
            print(message.content)
            break

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )

            print(f"\n🔧 Calling tool: {tool_name}")
            print(f"Arguments: {arguments}")

            function = available_functions.get(tool_name)

            if not function:
                result = {
                    "success": False,
                    "error": f"Unknown tool: {tool_name}"
                }

            else:
                try:
                    result = function(**arguments)
                    print("✅ Tool executed")

                except Exception as e:
                    result = {
                        "success": False,
                        "error": str(e)
                    }

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })


if __name__ == "__main__":
    main()