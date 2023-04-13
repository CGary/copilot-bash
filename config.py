#!/usr/bin/python3
import os
import sys
from termcolor import colored

class Config:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if self.api_key is None:
            print(colored("This program requires an OpenAI API key to run. Please set the OPENAI_API_KEY environment variable. https://github.com/m1guelpf/plz-cli#usage", "red"))
            sys.exit(1)
        self.api_base = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
        self.shell = os.environ.get("SHELL", "")

    def write_to_history(self, code):
        history_file = ""
        if self.shell == "/bin/bash":
            history_file = os.path.join(os.environ.get("HOME"), ".bash_history")
        elif self.shell == "/bin/zsh":
            history_file = os.path.join(os.environ.get("HOME"), ".zsh_history")
        else:
            return

        with open(history_file, "a") as file:
            try:
                file.write(code + "\n")
            except:
                sys.exit(1)