import sys
from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageDraw
from PIL.Image import Resampling
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguement")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguements")
elif (sys.argv[1].endswith(".png") and sys.argv[2].endswith(".jpg")) or (sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".png")) :
    sys.exit("Input and Output have different extensions")
elif (sys.argv[1].endswith(".png") and sys.argv[2].endswith(".png")) or (sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg")) :
    input_pic = sys.argv[1]
    output_pic = sys.argv[2]
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input_pic) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output_pic)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")
else:
    sys.exit("Invalid input")

