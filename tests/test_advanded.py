
import os
from newpyproj.newpyproj import create_folders
from newpyproj.newpyproj import create_files
from newpyproj.newpyproj import create_template
from newpyproj.newpyproj import parse_args
from newpyproj.newpyproj import folders
from newpyproj.newpyproj import root_files, project_files, test_files
from newpyproj.support import content_dict

class TestFolderCreation:
    def basic_creation(self, testname):
        create_folders(testname)
        assert os.path.split(os.getcwd())[1] == testname, "Root Folder not created"
        assert os.path.isdir(testname), "Project Folder not created"
    
    def test_create(self, tmpdir):
        os.chdir(tmpdir)
        self.basic_creation('projectnametest')

    def test_create_inside(self, tmpdir):
        os.chdir(tmpdir)
        os.mkdir('projectnametestinside')
        os.chdir('projectnametestinside')
        self.basic_creation('projectnametestinside')
    
    def test_create_space(self, tmpdir):
        os.chdir(tmpdir)
        self.basic_creation('project name test')

    def test_non_standard(self, tmpdir):
        os.chdir(tmpdir)
        self.basic_creation('prôjéçãonametest')
        os.chdir('..')
        self.basic_creation('досвидания')
        os.chdir('..')
        self.basic_creation('项目名称测试')


class TestFileCreation:
    def basic_creation(self, testname):
        create_folders(testname)
        create_files(testname)
        assert os.path.split(os.getcwd())[1] == testname, "Root Folder not created"
        assert os.path.isdir(testname), "Project Folder not created"
        for folder in folders:
            assert os.path.isdir(folder), "Folder ({folder}) not created"
        for file in root_files:
            assert os.path.isfile(file), f"Root file not found: {file}"
        for file in project_files:
            assert os.path.isfile(os.path.join(testname, file)), f"Project file not found: {file}"
        for file in test_files:
            assert os.path.isfile(os.path.join('tests', file)), f"Test file not found: {file}"
    
    def test_create_files(self, tmpdir):
        os.chdir(tmpdir)
        self.basic_creation('projectnametest')
class TestCreationModification:
    def basic_creation(self, testname, args):
        create_folders(testname, args)
        create_files(testname, args)
    
    def test_cli(self, tmpdir):
        os.chdir(tmpdir)
        arguments = parse_args(['projecttest', '-c'])
        self.basic_creation('projecttest', arguments)
        assert os.path.isfile('cli.py') and os.path.isfile(os.path.join('projecttest', 'cli.py')), "Cli file not created when argument given"

    def test_gui(self, tmpdir):
        os.chdir(tmpdir)
        arguments = parse_args(['projecttest', '-g'])
        self.basic_creation('projecttest', arguments)
        assert os.path.isfile('gui.py') and os.path.isfile(os.path.join('projecttest', 'gui.py')), "Gui file not created when argument given"

    def test_docs(self, tmpdir):
        os.chdir(tmpdir)
        arguments = parse_args(['projecttest', '-d'])
        self.basic_creation('projecttest', arguments)
        assert not os.path.isdir('docs'), "Docs folder not supressed when argument given"
    
    def test_tests(self, tmpdir):
        os.chdir(tmpdir)
        arguments = parse_args(['projecttest', '-t'])
        self.basic_creation('projecttest', arguments)
        assert not os.path.isdir('tests'), "Tests folder not supressed when argument given"

    def test_resources(self, tmpdir):
        os.chdir(tmpdir)
        arguments = parse_args(['projecttest', '-r'])
        self.basic_creation('projecttest', arguments)
        assert os.path.isdir('resources'), "Resources folder not created when argument given"

class TestTemplate:
    def basic_creation(self, testname, args):
        create_folders(testname, args)
        create_files(testname, args)
        create_template(testname, args)
    
    def basic_fileloading(self, testname, args):
        file_content = {'ignore': open('.gitignore','r').read(),
                        'readme': open('README','r').read(),
                        'license': open('LICENSE','r').read(),
                        'setup': open('setup.py','r').read(),
                        'cli': open('cli.py','r').read(),
                        'gui': open('gui.py','r').read(),
                        'init': open(os.path.join(testname, '__init__.py'),'r').read(),
                        'support': open(os.path.join(testname, 'support.py'),'r').read(),
                        'project': open(os.path.join(testname, testname + '.py'),'r').read(),
                        'test_advanced': open(os.path.join('tests', 'test_advanced.py'),'r').read(),
                        'test_basic': open(os.path.join('tests', 'test_basic.py'),'r').read(),
                        'cli2': open(os.path.join(testname, 'cli.py'),'r').read(),
                        'gui2': open(os.path.join(testname, 'gui.py'),'r').read()}
        
        return file_content
    
    def test_shebang(self, tmpdir):
        os.chdir(tmpdir)
        arguments = parse_args(['projecttest', '-g', '-c']) # includes all files that need a shebang
        self.basic_creation('projecttest', arguments)
        file_content = self.basic_fileloading('projecttest', arguments)
        for content in [file_content['project'], file_content['gui'], file_content['gui2'], file_content['cli'], file_content['cli2']]:  
            assert content_dict['shebang'] in content, "Shebang insertion in templates failed"
    
    def test_content(self, tmpdir):
        os.chdir(tmpdir)
        arguments = parse_args(['projecttest', '-g', '-c']) # includes all files that need a shebang
        self.basic_creation('projecttest', arguments)
        file_content = self.basic_fileloading('projecttest', arguments)
        for content in [file_content['project'], file_content['gui'], file_content['gui2'], file_content['cli'], file_content['cli2']]: 
            assert content_dict['shebang'] in content, "Template creation failed"

    def test_templatesupression(self, tmpdir):
        os.chdir(tmpdir)
        arguments = parse_args(['projecttest', '-g', '-c', '-s', '--template']) # includes all files that have templates
        self.basic_creation('projecttest', arguments)
        file_content = self.basic_fileloading('projecttest', arguments)
        for file in file_content:
            assert file_content[file] == '', "Template file content supression failed"
