import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test", prompt="Enter your username: ")
USER_INP2 = simpledialog.askstring(title="Test", prompt="Enter a song: ")



# check it out+
print("Username: ", USER_INP)
print("Song: ", USER_INP2)