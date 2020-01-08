# Intro to Computer Science Course-Projects
Course projects that used the language Python

Calcudoku
This project solves 5x5 Sodoku puzzles:
The rows and columns cannot have duplicates and only the numbers 1 through 5
The sum of the numbers in a predetermined cluster equals the number in the top left part of the cluster
Method:
This program solves the puzzle using exhaustive search (brute force) approach

Crime Time:
This program reads and writes records to a file from given tab-separated value files, each with their own one-line header.
The final file written combines the information from the two provided files (times.tsv and crimes.tsv) by eliminating files that are not a robbery and parsing the lines and comparing IDs. 
Computer Science Fundamentals Used:
Classes, objects, sort and search algorithms, Python file I/O functions.

Moonlander 
This program simulates landing the Lunar Module on the moon. It starts with zero velocity at an altitude and fuel level given by the user. Gravity accelorates it towards the moon. The user enters 0-9 to control the thruster rate of fuel flow. The goal is to land with a velocity between 0 and -1 meters per second using the least amount of fuel possible. 
Computer Science Fundamentals Used:
Functions and I/O

PixelMagic - Final Project
  Hidden Image:
  This program accepts the name of a P3 ppm file and mutates the red component of the pixels by 10, and sets the value of the blue and green components equal to the red value. This reveals a hidden image. 
  Fade:
  This program accepts the name of a P3 ppm file, the row and column of the fade center, and the fade radius and will output to a file named faded.ppm. It multiplies the color components of the pixel by the (radius - distance) / radius.
  Blur:
  Takes two command line arguments: the name of the image file and the "reach" used in calculating how blurred the image will become. For each pixel, it calculates the average over every color component of the nearby pixels and sets the color value of the current pixel to that number. The reach is the number of neighboring pixels away from the initial pixel included in the calculation. 
Computer Science Fundamentals Used:
Command line arguments, error handling, etc

Word Search
This program finds words hidden in a string. The words are hidden in the puzzle grid forward, backward, upward, and downward. It uses dimension conversion to find the row and column of the word and inverses the puzzle to check to see if the word is located in the puzzle backward or upward. 
Computer Science Fundamentals Used:
String operations, dimension conversion
