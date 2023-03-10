# using opencv-python = "==4.5.5.62" because of autocomplete issues with PyCharm intellisense
"""
a script to convert images of any format to the standard .png format
run it as -- python convert-to-png.py <input-directory> <output-directory>
"""

import os
import sys

import cv2 as cv

# print(cv.__version__)

input_folder = sys.argv[1]
output_folder = sys.argv[2]

files_list = os.listdir(f".\\{input_folder}")

if not os.path.exists(f".\\{output_folder}"):
    os.mkdir(f".\\{output_folder}")


def convert_to_png(source_directory, destination_directory):
    for file in files_list:
        image = cv.imread(f".\\{source_directory}{file}", cv.IMREAD_COLOR)
        only_file_name = os.path.splitext(file)[0]
        # print(only_file_name)
        cv.imwrite(f".\\{destination_directory}{only_file_name}.png", image)


convert_to_png(input_folder, output_folder)
