#!/usr/bin/env python

import os

def print_hello(name):
    """Say hello to someone!

    :param name: The name of the person to say hello to.
    :type name: str
    """

    print("Hello {0}!".format(name))

def get_data_dir():
    """Read the path to the data directory from the project environment variable."""

    try:
        data_dir = os.environ['PROJECT_DATA_DIR']
    except KeyError:
        raise KeyError("Please set the PROJECT_DATA_DIR environment variable in your env.sh file.")

    if (not os.path.isdir(data_dir)):
        raise NotADirectoryError("The path in PROJECT_DATA_DIR does not exist. Check your env.sh file.")

    return data_dir
