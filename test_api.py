#!/usr/bin/env python3
import openai
import os
from dotenv import dotenv_values

base_folder = os.path.dirname(__file__)
config = dotenv_values(base_folder + "/.env")
openai.api_key = config["OPENAI_API_KEY"]

# list models
models = openai.Model.list()
if not models:
    print("No models found")
    exit(0)

# print the first model's id
print(models.data[0].id)

# create a chat completion
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is the capital of Belgium?"}],
)
if not chat_completion.choices:
    print("No chat completions found")
    exit(0)

# print the chat completion
print(chat_completion.choices[0].message.content)
