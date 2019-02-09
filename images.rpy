# Define all images here.

image skip = "Skip.png"

image opening_text = ParameterizedText(xalign=0, yalign=0.5, xoffset=165)

image next = "Next.png"

image laffey = im.Scale("Laffey.png", 609.6, 819.2)
image laffey dark = im.MatrixColor(im.Scale("Laffey.png", 609.6, 819.2), im.matrix.brightness(-0.6))

image mccall = im.Scale("Mccall.png", 643.2, 629.6)
image mccall dark = im.MatrixColor(im.Scale("Mccall.png", 643.2, 629.6), im.matrix.brightness(-0.6))

image long island = im.Scale("Long_Island.png", 648.8, 819.2)
image long island dark = im.MatrixColor(im.Scale("Long_Island.png", 648.8, 819.2), im.matrix.brightness(-0.6))

image san diego = im.Scale("San_Diego.png", 539.2, 819.2)
image san diego dark = im.MatrixColor(im.Scale("San_Diego.png", 539.2, 819.2), im.matrix.brightness(-0.6))
