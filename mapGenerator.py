from PIL import Image
import numpy as np
from tkinter import filedialog
import pyperclip

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() 
filename = askopenfilename() 


map = Image.open(filename)
table = np.array(map)


cArr = "uint8_t grid[100][100] = {"


for r in table:
    cArr = cArr + "{"
    for c in r:
        if(c == 0):
            a = 1
        else:
            a = 0
        cArr = cArr + str(a) + ", "

    cArr = cArr + "},"
cArr = cArr + ("};")
pyperclip.copy(cArr)
print(cArr)
