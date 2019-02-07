# Define all images here.

image opening_text = ParameterizedText(xalign=0, yalign=0.5, xoffset=165)

image laffey = im.Scale("Laffey.png", 495.3, 665.6)
image laffey dark = im.MatrixColor(im.Scale("Laffey.png", 495.3, 665.6), im.matrix.brightness(-0.6))

image mccall = im.Scale("Mccall.png", 522.6, 511.6)
image mccall dark = im.MatrixColor(im.Scale("Mccall.png", 522.6, 511.6), im.matrix.brightness(-0.6))

image long island = im.Scale("Long_Island.png", 527.1, 665.6)
image long island dark = im.MatrixColor(im.Scale("Long_Island.png", 527.1, 665.6), im.matrix.brightness(-0.6))

image san diego = im.Scale("San_Diego.png", 438.1, 665.6)
image san diego dark = im.MatrixColor(im.Scale("San_Diego.png", 438.1, 665.6), im.matrix.brightness(-0.6))
