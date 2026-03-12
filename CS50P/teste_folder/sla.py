import os, sys
from PIL import Image

### pra identificar os formato:
#for infile in sys.argv[1:]:
    #f, e = os.path.splitext(infile)
    #outfile = f + ".jpg"

image = Image.open(sys.argv[1])
shirt = Image.open(sys.argv[2])

image.paste(shirt, shirt)
image.save(sys.argv[3])
image.show()
