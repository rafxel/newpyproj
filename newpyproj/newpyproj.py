#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

folders = {'docs':'', 'tests':''}
root_files = {'.ignore':'', 'cli.py':'', 'gui.py':'', 'README':'', 'LICENSE':'', 'setup.py':''}
project_files = {'__init__.py':'', 'support.py':''}
test_files = {'test_advanced.py':'', 'test_basic.py':''}

def parse_args(args):
    """Parse command line arguments

    Best use is to import with the sys module: sys.argv[1:]
    * first element is script name

    Arguments:
        args {list} -- Arguments from the command line

    Returns:
        argparse.Namespace -- returns the parsed arguments
    """
    parser = argparse.ArgumentParser(prog='newpyproj', description='Creates a new python project folder')
    parser.add_argument('project_name', help='Creates a command line interface project')
    parser.add_argument('-c', '--cli', action='store_true', help='Creates a command line interface project')
    parser.add_argument('-g', '--gui', action='store_true', help='Creates a graphical user interface project')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
    parser.add_argument('-t', '--test', action='store_false', help='Supress test folders and files')
    parser.add_argument('-d', '--doc', action='store_false', help='Supress doc folders and files')
    
    return parser.parse_args(args)

def create_folders(project_name, args):
    """Creates project folders from a list

    Arguments:
        project_name {str} -- Name of the python project
        args {list} -- List of arguments to be used when creating folders
    """
    pass

def create_files(project_name, args):
    """Creates project files from a list

    Arguments:
        project_name {str} -- Name of the python project
        args {list} -- List of arguments to be used when creating files
    """
    pass

def initiate_git(project_name):
    """Initializes git in project folder
    TODO: Go into the directory containing the project.
    TODO: Type git init .
    TODO: Type git add to add all of the relevant files.
    TODO: You'll probably want to create a . gitignore file right away, to indicate all of the files you don't want to track. Use git add . gitignore , too.
    TODO: Type git commit.
    Arguments:
        project_name {str} -- Name of the python project
    """
    pass