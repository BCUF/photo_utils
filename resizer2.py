###
# Copyright BCU Fribourg 2019
# Project: photo_utils
# File: resizer.py
# Author: Nicolas Stulz
###

import os, sys
from pathlib import Path
import argparse
from PIL import Image

# RUN example: python resizer.py <photo_in_name.tif> max_size <photo_out_name.jpg> <out_format>
#              python resizer.py JATH_52577.tif 2000 jath.jpg

# print('Number of arguments:', len(sys.argv), 'arguments.') ## remove after.......
# print('Argument List:', str(sys.argv)) ## remove after.......

# if len(sys.argv) != 4:
#     if len(sys.argv) < 4:
#         print("Arguments missing...")
#         exit(0)
#     else:
#         print("Too much arguments...")
#     print("Try: ")
#     print("python resizer.py <input_file.tif> 2000 <output_file.jpg>")
#     exit(0)
# else:

# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

original_photo_name = sys.argv[1]

max_size = int(sys.argv[2])

new_filename = os.path.splitext(sys.argv[3])[0]
extension = os.path.splitext(sys.argv[3])[1]

size_info = "_2k"

default_format = "JPEG"

try:

    img = Image.open(original_photo_name, mode='r')

    img.thumbnail((max_size, max_size), Image.ANTIALIAS)

    resized_photo_name = new_filename + size_info + extension

    if original_photo_name == resized_photo_name:
        print("Input and output file has same name and path...")
        print("Cannot resize...")
        sys.exit(0)
    else:
        img.save(resized_photo_name, default_format, quality=100)

    img = Image.open(resized_photo_name, mode='r')

    print("\n############################################################")
    print("#")
    print("#    Photo " + img.filename + " has been saved...")
    print("#")
    print("############################################################\n")

    print("\n############################################################")
    print("#")
    print("#    Photo " + img.filename + " has been saved...")
    print("#")
    print("#    -----------  infos   -----------------")
    print("#")
    print("#    size:        " + str(img.size[0]) + " x " + str(img.size[1]))
    # if img.info["compression"]:
    # print("#    compression: " + str(img.info["compression"]))
    #print("#    dpi:         " + str(img.info["dpi"]))
    print("#    mode:        " + str(img.mode))
    print("#    format:      " + str(img.format))
    print("#")
    print("############################################################\n")

except IOError:
    print("Cannot resize for '%s'" % original_photo_name)

def resize_photo(photo, max_width, max_height):
    photo_width, photo_height = photo.size

    # if the photo width is the longuest side
    if photo_width > photo_height:
        ratio = max_width / photo_width
        photo_width = max_width
        photo_height = int(photo_height * ratio)

    else:
        ratio = max_height / photo_height
        photo_height = max_height
        photo_width = int(photo_width * ratio)

    return photo.resize((photo_width, photo_height), Image.ANTIALIAS)

# original_photo_name = sys.argv[1]

# max_size = int(sys.argv[2])

# new_filename = os.path.splitext(sys.argv[3])[0]
# extension = os.path.splitext(sys.argv[3])[1]

# size_info = "_2k"

# default_format = "JPEG"

# try:

#     img = Image.open(original_photo_name, mode='r')

#     img.thumbnail((max_size, max_size), Image.ANTIALIAS)

#     resized_photo_name = new_filename + size_info + extension

#     if original_photo_name == resized_photo_name:
#         print("Input and output file has same name and path...")
#         print("Cannot resize...")
#         sys.exit(0)
#     else:
#         new_img = img.save(resized_photo_name, default_format, quality=100)

#     print("\n############################################################")
#     print("#")
#     print("#    Photo " + new_img.filename + " has been saved...")
#     print("#")
#     print("#    -----------  infos   -----------------")
#     print("#")
#     print("#    size:        " + str(new_img.size[0]) + " x " + str(new_img.size[1]))
#     # if img.info["compression"]:
#     #     print("#    compression: " + str(img.info["compression"]))
#     print("#    dpi:         " + str(new_img.info["dpi"]))
#     print("#    mode:        " + str(new_img.mode))
#     print("#    format:      " + str(new_img.format))
#     print("#")
#     print("############################################################\n")

# except IOError:
#     print("Cannot resize for '%s'" % original_photo_name)