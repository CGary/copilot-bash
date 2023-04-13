#!/usr/bin/python3

import sys
import os
import json
import argparse
import requests
import subprocess
from typing import List
from questionary import prompt
import platform

# Define command line arguments
parser = argparse.ArgumentParser(
    description='Generate and execute a command using OpenAI\'s GPT-3 API')
parser.add_argument('prompt', metavar='PROMPT', type=str, nargs='+',
                    help='Description of the command to execute')
parser.add_argument('-y', '--force', action='store_true',
                    help='Run the generated program without asking for confirmation')

# Read the API key from environment variable
# API_KEY = os.getenv('OPENAI_API_KEY')
API_KEY = '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'
if not API_KEY:
    print('Error: OPENAI_API_KEY environment variable not set', file=sys.stderr)
    sys.exit(1)

# Define the API endpoint
API_BASE = 'https://api.openai.com/v1'

# Define the GPT-3 model parameters
MODEL = 'davinci'
TOP_P = 1
STOP = '```'
TEMPERATURE = 0
SUFFIX = '\n```'
MAX_TOKENS = 1000
PRESENCE_PENALTY = 0
FREQUENCY_PENALTY = 0


def main(args: argparse.Namespace):
    prompt_str = ' '.join(args[1:])
    prompt = build_prompt(prompt_str)
    headers = {'Authorization': 'Bearer ' + API_KEY}
    endpoint = f'{API_BASE}/chat/completions'

    # Send a request to GPT-3 API to generate a command
    print('Generating your command...')
    data = {'model': MODEL, 'prompt': prompt, 'temperature': TEMPERATURE,
            'max_tokens': MAX_TOKENS, 'top_p': TOP_P, 'frequency_penalty': FREQUENCY_PENALTY,
            'presence_penalty': PRESENCE_PENALTY, 'stop': STOP, 'suffix': SUFFIX}
    try:
        response = requests.post(endpoint, headers=headers, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)

    print('HERE!!!!!!!')
    # # Extract the generated command from the response
    # response_data = response.json()
    # if not response_data.get('choices'):
    #     spinner.stop()
    #     print('Error: Failed to generate a command', file=sys.stderr)
    #     sys.exit(1)

    # command = response_data['choices'][0]['text'].strip()

    # # Print the generated command
    # spinner.stop_and_persist('✔'.green(), 'Got some code!'.green())
    # print(command)

    # # Execute the command
    # if args.force or prompt_yes_no('Run the generated program?'):
    #     try:
    #         spinner = (Spinners.bouncing_bar, 'Executing...')
    #         output = subprocess.check_output(['bash', '-c', command], stderr=subprocess.STDOUT)
    #     except subprocess.CalledProcessError as e:
    #         spinner.stop()
    #         print(f'Error: {e}', file=sys.stderr)
    #         sys.exit(1)

    #     if output:
    #         spinner.stop_and_persist('✔'.green(), 'Command ran successfully'.green())
    #         print(output.decode().strip())
    #     else:
    #         spinner.stop_and_persist('✖'.red(), 'The program threw an error.'.red())
    #         sys.exit(1)


def build_prompt(prompt: str) -> str:
    os_hint = ""
    if platform.system() == "Darwin":
        os_hint = " (on macOS)"
    elif platform.system() == "Linux":
        os_hint = " (on Linux)"

    return f"{prompt}{os_hint}:\n```bash\n#!/bin/bash\n"


main(sys.argv)
