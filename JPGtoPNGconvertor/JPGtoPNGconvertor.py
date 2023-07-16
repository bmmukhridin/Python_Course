import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check is new/ exist, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop through Pokidex,
for filename in os.listdir(image_folder):
    x = os.listdir(image_folder[1], '.DS_Store')
    print(x)
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]

    # convert images to png
    # img.save(f'{output_folder}{clean_name}.png', "png")
    # print("all done!")
# save to new folder


# img = os.listdir("../images")
# clean_name = os.path.splitext(img)
# print(clean_name)
