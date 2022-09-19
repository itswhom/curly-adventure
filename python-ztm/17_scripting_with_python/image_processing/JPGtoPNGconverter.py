from lib2to3.pytree import convert
from PIL import Image
import sys
import os
import pathlib

# the run line:
# python3 name.py Pokedex/ new/

# grab first and second argument
source_dir = str(sys.argv[1])
destination_dir = str(sys.argv[2])

# check if new/ exists, if not create it
if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)

# loop through pokedex/
for mon in os.listdir(source_dir):
    source_image = Image.open(source_dir + mon)
    stem = pathlib.Path(mon).stem
    # save to new folder as png
    source_image.save(destination_dir + stem + '.png')
    
