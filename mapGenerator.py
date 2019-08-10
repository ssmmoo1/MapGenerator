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

rows = str(len(table))
cols = str(len(table[0]))
cArr = "uint8_t grid["+rows+"]["+cols+"] = {"


for r in table:
    cArr = cArr + "{"
    for c in r:

        if c[0] == 0 and c[1] == 0 and c[2] == 0:

            a = 1
        else:
            a = 0
        cArr = cArr + str(a) + ", "

    cArr = cArr + "},"
cArr = cArr + ("};")
pyperclip.copy(cArr)
print(cArr)
