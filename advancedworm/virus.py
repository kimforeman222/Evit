import tkinter as tk
import os
from pathlib import Path
from PIL import Image, ImageTk
parent = tk.Tk()
parent.title("Application Title")
image_path = "OIP.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(parent, image=image)
image_label.pack()
parent.mainloop()

pink = Path('OIP.jpg')
contents = pink.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)
pink = Path('/home/Documents/Github/Evit/advancedworm/OIP.jpg')
print('OIP.jpg')

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