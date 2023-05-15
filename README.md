# bashGPT

![bash GPT](assets/bashgpt.jpg)

An AI assistant in your CLI. Ask it to do something in your terminal, and it will select the best CLI command to do it, and execute it.

## Usage

```
------------------- START bashgpt -------------------
Use 'quit' or 'q' to exit the script.
QUERY  : what is the time
COMMAND: «date +'%r'» ...
EXPLAIN:  The time is 10:21:02 PM.
 
QUERY  : q
------------------- FINISH bashgpt -------------------
```

## Installation

with [basher](https://github.com/basherpm/basher)

```bash
basher install pforret/gitploy
bashgpt install
```

or with `git`

```bash
git clone https://github.com/pforret/bashgpt.git
cd bashgpt
./bashgpt.sh install
✅  python-dotenv is installed
✅  revChatGPT is installed
# get an OpenAI API key from https://platform.openai.com/account/api-keys
```
