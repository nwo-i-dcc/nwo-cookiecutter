#!/usr/bin/env python

import os


class Paths:
    """This class contains the paths defined in this research project. The paths are defined at first as environment variables
       in env.sh. This class makes them available in Python."""


    def __init__(self):

        try:
            self.project_dir = os.environ['PROJECT_DIR']
        except KeyError:
            print("Please set the PROJECT_DIR environment variable to your project directory (see env.sh).")
            return

        try:
            self.project_data_dir = os.environ['PROJECT_DATA_DIR']
        except KeyError:
            print("Please set the PROJECT_DATA_DIR environment variable to your project data directory (see env.sh).")
            return
