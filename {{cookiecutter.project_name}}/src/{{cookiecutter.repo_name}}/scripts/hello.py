#!/usr/bin/env python

import argparse
from {{ cookiecutter.repo_name }}.functions import print_hello, get_data_dir

def hello():
    """Say hello to someone!"""

    # Get location of project directory from PROJECT_DATA_DIR
    data_dir = get_data_dir()

    # Get name from the command line
    parser = hello_arguments()
    args = parser.parse_args()

    # Call function to print the greeting
    print_hello(args.name)

def hello_arguments():
    """Get the name for hello from the command line using argparse."""
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of the person to say hello to.', type=str)
    return parser

if __name__ == "__main__":
    hello()
