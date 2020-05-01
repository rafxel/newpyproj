#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import subprocess

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
    parser.add_argument('-r', '--resources', action='store_true', help='Include resources folder')
    parser.add_argument('-s', '--shebang', action='store_false', help='Supress shebang line in files')
    parser.add_argument('-t', '--test', action='store_false', help='Supress test folders and files')
    parser.add_argument('-d', '--doc', action='store_false', help='Supress doc folders and files')
    
    return parser.parse_args(args)

def create_folders(project_name, args={}):
    """Creates project folders from a list

    Arguments:
        project_name {str} -- Name of the python project
        args {list} -- List of arguments to be used when creating folders
    """
    
    creation_folders = folders.copy()
    creation_folders[project_name] = ''

    if 'docs' in args and \
        args['docs'] == False:
        del(creation_folders['docs'])
    if 'tests' in args and \
        args['tests'] == False:
        del(creation_folders['tests'])

    # check if not already inside folder with project name
    if os.path.split(os.getcwd())[1] != project_name:
        os.mkdir(project_name)
        os.chdir(project_name)

    for folder in creation_folders:
        os.mkdir(folder)
    


def create_files(project_name, args={}):
    """Creates project files from a list

    Arguments:
        project_name {str} -- Name of the python project
        args {list} -- List of arguments to be used when creating files
    """
    def open_files(file_list):
        for file_name in file_list:
            open(file_name, 'w').close()

    creation_project_files = project_files.copy()
    creation_project_files[project_name + '.py'] = ''

    # check if in root and folders exist
    if os.path.split(os.getcwd())[1] == project_name and \
        os.path.isdir(project_name):
        
        open_files(root_files)
        os.chdir(project_name)
        open_files(creation_project_files)
        os.chdir('..')
        os.chdir('tests')
        open_files(test_files)
        os.chdir('..')
    else:
        raise OSError('Folder not found')



def initiate_git(project_name):
    """Initializes git in project folder

    Arguments:
        project_name {str} -- Name of the python project
    """
    initial_folder = os.getcwd()
    os.chdir(project_name)
    try:
        subprocess.call(['git', 'init'])
        subprocess.call(['git', 'add', '.'])
        subprocess.call(['git', 'commit', '-m', 'First Commit'])
    except OSError as e:
        print('GIT not available')
    
    os.chdir(initial_folder)
