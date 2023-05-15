#!/usr/bin/env python3
from dotenv import dotenv_values
from revChatGPT.V3 import Chatbot
import json
import subprocess
import os

base_folder = os.path.dirname(__file__)
config = dotenv_values(base_folder + "/.env")
debug = config["DEBUG"] == "true"
system_prompt_file = base_folder + "/" + config["SYSTEM_PROMPT_FILE"]
if not os.path.isfile(system_prompt_file):
    print("system prompt not found")
    exit(0)

openai_api_key = config["OPENAI_API_KEY"]
openai_organisation = config["OPENAI_ORGANIZATION"]


class colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    FAIL = "\033[91m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    OKBLUE = "\033[94m"
    HEADER = "\033[95m"
    OKCYAN = "\033[96m"


"""
Opens the system_prompt.txt file that contains the initial prompt sent to ChatGPT. 
This is where the magic happens.
"""
with open(system_prompt_file, "r") as sys_prompt:
    system_prompt_text = sys_prompt.read()


# Connect to the openAI API using your API key
chatbot = Chatbot(api_key=openai_api_key, system_prompt=system_prompt_text)

print(colors.HEADER + "Use 'quit' or 'q' to exit the script." + colors.RESET)
# Main loop
while True:
    prompt = input("QUERY  : ")

    # This part checks whether or not the user typed exit or quit to exit the script
    if prompt.lower().strip() in ["exit", "quit", "x", "q"]:
        exit(0)

    # And here the query/request/question is sent to chatGPT
    response = chatbot.ask("Human: " + prompt)

    # This is in a loop for future proofing reasons in case
    # chatGPT decides to run another command after running a previous
    # one, before responding to the user so that the script is not broken.

    while True:
        if debug:
            print(response)
        if "@Backend" in response:
            # Extract the command that chatGPT wants to run and deserialize it.
            res = response.split("@Backend")[1]
            if debug:
                print(res)
            json_str = json.loads(res)
            command = json_str["command"]

            print("COMMAND: «" + colors.WARNING + command + colors.RESET + "» ...")
            # Run the command and store it's outputs for later
            p = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
            )
            output, err = p.communicate()
            # Get the exit code
            exit_code = p.wait()
            # Send the command results to chatGPT so it can be interpreted by it.
            response = chatbot.ask(
                'Backend: {"STDOUT":"%s", "EXITCODE":"%s"}' % (output, exit_code)
            )

        elif "@Human" in response:
            if debug:
                print(response)
            chatGPT_reply = (
                "EXPLAIN: " + colors.OKBLUE + response.split("@Human")[1] + colors.RESET
            )
            print(chatGPT_reply)
            break

        else:
            print("UNEXPECTED RESPONSE:: [%s]" % (response))
            break

    print(" ")
