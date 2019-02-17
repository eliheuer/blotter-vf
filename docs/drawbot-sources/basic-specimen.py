# Render this specimen with DrawBot3: http://www.drawbot.com/
# from DrawBot import *
from drawBot import *
import math
import os


# Basic variables  (width, height, margin, frame-count ):
W, H, M, F = 1024, 1024, 128, 32


# Load font and print font info:
os.chdir("..")
os.chdir("..")
# font("fonts/Blotter-VF.ttf")
font("fonts/Blotter-VF.ttf")
for axis, data in listFontVariations().items():
    # Get axis info from font
    print((axis, data)) 


def grid(inc):
    """
    Draw grid from a given increment "inc":
    """
    # Set grid color
    stroke(0.3)
    stpX, stpY = 0, 0
    incX, incY = inc, inc

    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY


# Draw page
newPage(W, H)
fill(0)
rect(0, 0, W, H)

# Draw the grid
grid(32)

# Basic Style
stroke(None)
fill(1)
fontSize(80)
varWght = 300

text("a b c d e f g h i j k l m n o p q r s t u v w x y z", 100, 100)


# Save GIF
os.chdir("docs")
os.chdir("images")
saveImage("basic-specimen.gif")
os.chdir("..")
os.chdir("..")
