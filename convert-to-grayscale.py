# using opencv-python = "==4.5.5.62" because of autocomplete issues with PyCharm intellisense
"""
a script to convert images to a grayscale format to assist with finding contours
run it as -- python convert-to-grayscale.py <input-directory> <output-directory>
"""

import os
import sys

import cv2 as cv

# print(cv.__version__)

input_folder = sys.argv[1]
output_folder = sys.argv[2]

images_list = os.listdir(f".\\{input_folder}")

if not os.path.exists(f".\\{output_folder}"):
    os.mkdir(f".\\{output_folder}")


def convert_to_grayscale(source_directory, destination_directory):
    for file in images_list:
        image = cv.imread(f".\\{source_directory}{file}", cv.IMREAD_COLOR)
        grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        cv.imwrite(f".\\{destination_directory}{file}", grayscale)


convert_to_grayscale(input_folder, output_folder)
