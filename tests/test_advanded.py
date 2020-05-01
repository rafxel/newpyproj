from newpyproj.newpyproj import create_folders
from newpyproj.newpyproj import create_files
from newpyproj.newpyproj import folders
from newpyproj.newpyproj import root_files, project_files, test_files
import os

class TestFolderCreation:
    def assertion_factory(self, testname):
        create_folders(testname)
        assert os.path.split(os.getcwd())[1] == testname, "Root Folder not created"
        assert os.path.isdir(testname), "Project Folder not created"
    
    def test_create(self, tmpdir):
        os.chdir(tmpdir)
        self.assertion_factory('projectnametest')
        os.chdir('..')

    def test_create_inside(self, tmpdir):
        os.chdir(tmpdir)
        os.mkdir('projectnametestinside')
        os.chdir('projectnametestinside')
        self.assertion_factory('projectnametestinside')
        os.chdir('..')
    
    def test_create_space(self, tmpdir):
        os.chdir(tmpdir)
        self.assertion_factory('project name test')
        os.chdir('..')

    def test_non_standard(self, tmpdir):
        os.chdir(tmpdir)
        self.assertion_factory('prôjéçãonametest')
        os.chdir('..')
        self.assertion_factory('досвидания')
        os.chdir('..')
        self.assertion_factory('项目名称测试')
        os.chdir('..')

class TestFileCreation:
    def assertion_factory(self, testname):
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
        self.assertion_factory('projectnametest')
class TestCreationModification:
    def test_cli(self):
        pass

    def test_gui(self):
        pass

class TestFolderReading:
    def test_pontuar_valor(self):
        pass

class TestFolderDeleting:
    def test_pontuar_valor(self):
        pass

class TestDocumentation:
    def test_pontuar_valor(self):
        pass
