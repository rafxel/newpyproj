from newpyproj.newpyproj import folders
from newpyproj.newpyproj import root_files, project_files, test_files
from newpyproj.newpyproj import parse_args

class TestFolders:
    def test_minimum_folders(self):
        minimum_folders = ['docs', 'tests']
        for folder in minimum_folders:
            assert folder in folders, f"Missing one of the minimum folders: {folder}"

class TestFiles:
    def root_files(self):
        minimum_root = ['.ignore', 'cli.py', 'gui.py', 'README', 'LICENSE', 'setup.py']
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
        dic_vars = vars(parser)
        assert dic_vars['project_name'] == 'projectnametest', "Project name argument in parser failed."

    def test_cli(self):
        parser = parse_args(['projectnametest', '-c'])
        dic_vars = vars(parser)
        assert dic_vars['cli'] == True, "Command line argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--cli'])
        dic_vars = vars(parser)
        assert dic_vars['cli'] == True, "Command line argument in parser failed."
    
    def test_gui(self):
        parser = parse_args(['projectnametest', '-g'])
        dic_vars = vars(parser)
        assert dic_vars['gui'] == True, "GUI argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--gui'])
        dic_vars = vars(parser)
        assert dic_vars['gui'] == True, "GUI argument in parser failed."
    
    def test_verbose(self):
        parser = parse_args(['projectnametest', '-v'])
        dic_vars = vars(parser)
        assert dic_vars['verbose'] == True, "Verbose argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--verbose'])
        dic_vars = vars(parser)
        assert dic_vars['verbose'] == True, "Verbose argument in parser failed."
    
    def test_test(self):
        parser = parse_args(['projectnametest', '-t'])
        dic_vars = vars(parser)
        assert dic_vars['test'] == False, "Test argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--test'])
        dic_vars = vars(parser)
        assert dic_vars['test'] == False, "Test argument in parser failed."
    
    def test_doc(self):
        parser = parse_args(['projectnametest', '-d'])
        dic_vars = vars(parser)
        assert dic_vars['doc'] == False, "Documentation argument abbreviation in parser failed."
        parser = parse_args(['projectnametest', '--doc'])
        dic_vars = vars(parser)
        assert dic_vars['doc'] == False, "Documentation in parser failed."
