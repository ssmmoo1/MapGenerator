# Bitmap to Array Converter

### This program converts black and white bitmaps into a C array of 1's and 0's

### Purpose:

I wrote this program to easily create maps for a 3D game I made in C that used raycasting to turn a 2D map into a 3D projection.The map is a 2D array with 1's and 0's which represent walls or empty space. I wanted to be able to draw the map in paint instead of manually placing 1's and 0's in the arrays. So this tool takes black and white drawings from paint and then converts the black and white data into the 2D array of 1's and 0's to represent the map in my game. This tool made it very convenient to copy and paste new maps into the code.

### Dependencies:

This program was written in python 3 and requires Pillow and Pyperclip to be installed.
Pillow is used to read the bitmap data and pyperclip is used to save the 2D array in C syntax to your clipboard for easy pasting.

```
pip install Pillow
pip install pyperclip
```

### How to use:

In an image editor like MS paint, set the size of the canvas to the size of the map you need. 1 pixel = 1 element in the array.
Fill in the canvas as black then use the eraser tool to draw the map. Black will get converted to a 1 and white will be a 0. 
Save the image as a 24 bit bitmap. This is the only file type that will work with the program.

Execute the script by opening it in an IDE and running it or open a command line in the same directory as the progam and type
```
python3 mapGenerator.py
```
You will be prompted to choose the bitmap file for conversion. This program will not change, delete or create files.
After the program is run, the output to the console will be a C array that holds the image data as 1's and 0's.
The array will also be copied into your clipboard so it can easily be pasted into your code.




