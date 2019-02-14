###
# Copyright BCU Fribourg 2019
# Project: photo_utils
# File: resizer.py
# Author: Nicolas Stulz
###

# example python resizer.py -i img/JATH_52577.tif -s 1100 -o img/xxx.jpg

import os, sys
from pathlib import Path
import argparse
from PIL import Image

FORMATS = {
    "jpg": {
        "mime":"JPEG",
        "ext":".jpg"
    },
    "png": {
        "mime":"PNG",
        "ext":".png"
    }
}

DEFAULT_FORMAT = "jpg"

def decor_print(max_length, s):
    x = int((max_length-len(s)) / 2)
    y = max_length - len(s) - x - 2
    print("#" + " " * x + s + " " * y + "#")

def convert_size_to_k(size):
    if size >= 1000:
        size //= 1000
        return "_".__add__(str(size)).__add__("k")

def main():

    parser = argparse.ArgumentParser(description='This program allows you to resize a picture')
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')

    required.add_argument('-i','--input', type=str,
        help='The input file name (and path if not current folder)', required=True)
    required.add_argument('-s','--size', type=int,
        help='The size of the longest side of the image', required=True)
    required.add_argument('-o','--output', type=str,
        help='The output file name (and path if not current folder)', required=True)

    optional.add_argument('-v','--verbosity', type=int,
        help='Set to 1 to print, set 0 to not print anything', default=1)
    optional.add_argument('-f','--format', type=str,
        help='Set the file format [jpg|png] default is jpg', default=DEFAULT_FORMAT)
    optional.add_argument('-d','--dimension', action="store_true", default=False,
        help='Just add -d to automatically add the longest side dimension to the resized image. Example for a x.jpg (2000x1500) -> x_2k.jpg')
    optional.add_argument('-c','--compare', action="store_true", default=False,
        help='Just add -c to compare the input and output file')

    parser._action_groups.append(optional)

    args = parser.parse_args()

    original_photo_name = args.input
    max_size = args.size
    output_name = args.output
    verb = args.verbosity

    img_format = args.format

    size_info = ""

    if args.dimension:
        size_info = convert_size_to_k(max_size)

    new_filename = os.path.splitext(output_name)[0]

    try:

        img = Image.open(original_photo_name, mode='r')

        dpi = img.info["dpi"]

        img.thumbnail((max_size, max_size), Image.ANTIALIAS)

        resized_photo_name = new_filename.__add__(size_info).__add__(FORMATS[img_format]["ext"])

        if original_photo_name == resized_photo_name:
            print("Input and output files are same...")
            print("Cannot resize...")
            sys.exit(0)
        else:
            img.save(resized_photo_name, FORMATS[img_format]["mime"], quality=100, dpi=dpi)

        img.close()

        if verb == 1 and args.compare is False:

            print("\n")
            decor_print(60, 57 * "#")
            decor_print(60, "")
            decor_print(60, "Photo " + resized_photo_name + " has been saved...")
            decor_print(60, "")
            decor_print(60, 57 * "#")
            print("\n")

        if args.compare:    #TODO Center the 2 columns

            in_img = Image.open(original_photo_name, mode='r')
            out_img = Image.open(resized_photo_name, mode='r')

            print("\n" + "#" * 60)
            decor_print(60, "Compare")
            decor_print(60, "")
            print("#    Name: " + in_img.filename + " |    " + out_img.filename)
            decor_print(60, "")
            decor_print(60, "")
            print("#    size:        " + str(in_img.size)+ " |    " + str(out_img.size))
            print("#    dpi:         " + str(in_img.info["dpi"])+ "    | " + str(out_img.info["dpi"]))
            print("#    mode:        " + str(in_img.mode)+ " |    " + str(out_img.mode))
            print("#    format:      " + str(in_img.format)+ " |    " + str(out_img.format))
            decor_print(60, "")
            print("#" * 60 + "\n")

    except IOError:
        print("Cannot resize for '%s'" % original_photo_name)

if __name__ == "__main__":
    main()