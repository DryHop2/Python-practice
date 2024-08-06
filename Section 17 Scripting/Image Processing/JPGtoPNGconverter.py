import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists; if not, create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through images and convert to PNG
for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

# save to new folder
