# bashGPT

![bash GPT](assets/bashgpt.jpg)

An AI assistant in your CLI. Ask it to do something in your terminal, and it will select the best CLI command to do it, and execute it.

## Usage

```
Program : bashgpt  by peter@forret.com
Version : v0.1.2 (May 15 21:57:54 2023)
Purpose : An ai assistant in your CLI
Usage   : bashgpt [-h] [-q] [-v] [-f] [-l <log_dir>] [-t <tmp_dir>] <action>
Flags, options and parameters:
-h|--help        : [flag] show usage [default: off]
-q|--quiet       : [flag] no output [default: off]
-v|--verbose     : [flag] also show debug messages [default: off]
-f|--force       : [flag] do not ask for confirmation (always yes) [default: off]
-l|--log_dir <?> : [option] folder for log files   [default: /Users/pforret/log/bashgpt]
-t|--tmp_dir <?> : [option] folder for temp files  [default: /tmp/bashgpt]
<action>         : [choice] action to perform  [options: run,install,test,check,env,update]
```

## Examples

```bash
------------------- START bashgpt -------------------
Use 'quit' or 'q' to exit the script.
QUERY  : what is the time
COMMAND: «date +'%r'» ...
EXPLAIN:  The time is 10:21:02 PM.
 
QUERY  : q
------------------- FINISH bashgpt -------------------

------------------- START bashgpt -------------------
Use 'quit' or 'q' to exit the script.
QUERY  : create a video that fades from white to black in 5 seconds
COMMAND: «ffmpeg -f lavfi -i color=white:s=1280x720:d=5 -f lavfi -i color=black:s=1280x720:d=5 
        -filter_complex "[0:v]fade=t=out:st=4:d=1:alpha=1[v0];[1:v]fade=t=in:st=0:d=1:alpha=1[v1];[v0][v1]concat=n=2:v=1:a=0" 
        output.mp4» ...
EXPLAIN:  The video has been created successfully.
 
QUERY  : q
------------------- FINISH bashgpt -------------------

bashgpt test
First model from OpenAI: whisper-1
Answer from OpenAI: The capital of Belgium is Brussels.
```

## Installation

with [basher](https://github.com/basherpm/basher)

```bash
basher install pforret/bashgpt
bashgpt install
✅  python-dotenv is installed
✅  revChatGPT is installed
# get an OpenAI API key from https://platform.openai.com/account/api-keys
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
