from newpyproj.newpyproj import folders
from newpyproj.newpyproj import root_files, project_files, test_files
from newpyproj.newpyproj import parse_args
from newpyproj.support import content_dict

class TestFolders:
    def test_minimum_folders(self):
        minimum_folders = ['docs', 'tests']
        for folder in minimum_folders:
            assert folder in folders, f"Missing one of the minimum folders: {folder}"

class TestFiles:
    def root_files(self):
        minimum_root = ['.gitignore', 'cli.py', 'gui.py', 'README', 'LICENSE', 'setup.py']
        for root_file in minimum_root:
            assert root_file in root_files, f"Missing one of the minimum root files: {root_file}"
    
    def project_files(self):
        minimum_project = ['__init__.py', 'support.py']
        for project_file in minimum_project:
            assert project_file in project_files, f"Missing one of the minimum project files: {project_file}"
    
    def test_files(self):
        minimum_test = ['test_advanced.py', 'test_basic.py']
        for test_file in minimum_test:
            assert test_file in test_files, f"Missing one of the minimum test files: {test_file}"

class TestArgparsing:
    def test_project_name(self):
        parser = parse_args(['projectnametest'])
        assert parser['project_name'] == 'projectnametest', "Project name argument in parser failed."

    def test_cli(self):
        parser = parse_args(['projectnametest', '-c'])
        assert parser['cli'] == True, "Command line argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--cli'])
        assert parser['cli'] == True, "Command line argument in parser failed."
    
    def test_gui(self):
        parser = parse_args(['projectnametest', '-g'])
        assert parser['gui'] == True, "GUI argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--gui'])
        assert parser['gui'] == True, "GUI argument in parser failed."
    
    def test_verbose(self):
        parser = parse_args(['projectnametest', '-v'])
        assert parser['verbose'] == True, "Verbose argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--verbose'])
        assert parser['verbose'] == True, "Verbose argument in parser failed."

    def test_pytest(self):
        parser = parse_args(['projectnametest', '-p'])
        assert parser['pytest'] == True, "Pytest argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--pytest'])
        assert parser['pytest'] == True, "Pytest argument in parser failed."

    def test_resources(self):
        parser = parse_args(['projectnametest', '-r'])
        assert parser['resources'] == True, "Resources argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--resources'])
        assert parser['resources'] == True, "resources argument in parser failed."

    def test_shebang(self):
        parser = parse_args(['projectnametest', '-s'])
        assert parser['shebang'] == False, "Shebang argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--shebang'])
        assert parser['shebang'] == False, "Shebang argument in parser failed."
    
    def test_test(self):
        parser = parse_args(['projectnametest', '-t'])
        assert parser['tests'] == False, "Test argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--tests'])
        assert parser['tests'] == False, "Test argument in parser failed."
    
    def test_doc(self):
        parser = parse_args(['projectnametest', '-d'])
        assert parser['docs'] == False, "Documentation argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--docs'])
        assert parser['docs'] == False, "Documentation in parser failed."

class TestContentdictionary:
    def test_contentdictionary(self):
        for item in ['projectfile',
                     'gitignore',
                     'cli',
                     'gui',
                     'cli2',
                     'gui2',
                     'readme',
                     'license',
                     'setup',
                     'init',
                     'support',
                     'test_advanced',
                     'test_basic',
                     'shebang']:
            assert item in content_dict, f"No corresponding entry in content dictionary, for {item} file."
