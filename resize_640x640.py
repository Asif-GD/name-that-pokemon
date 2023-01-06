# using opencv-python = "==4.5.5.62" because of autocomplete issues with PyCharm intellisense
"""
a script to resize images to a resolution of 640 x 640
run it as -- python resize_640x640.py <input-directory> <output-directory>
"""

import os
import sys

import cv2 as cv

# print(cv.__version__)

input_folder = sys.argv[1]
output_folder = sys.argv[2]
image_width = 640
image_height = 640
image_size = (image_width, image_height)

images_list = os.listdir(f".\\{input_folder}")

if not os.path.exists(f".\\{output_folder}"):
    os.mkdir(f".\\{output_folder}")


def resize_to_640x640(source_directory, destination_directory):
    for file in images_list:
        image = cv.imread(f".\\{source_directory}{file}", cv.IMREAD_COLOR)
        resized_image = cv.resize(image, image_size, interpolation=cv.INTER_LINEAR)
        cv.imwrite(f".\\{destination_directory}{file}", resized_image)


resize_to_640x640(input_folder, output_folder)

# image = cv.imread(".\\png-images\\001_bulbasaur.png", cv.IMREAD_COLOR)
# resized_image = cv.resize(image, image_size, interpolation=cv.INTER_LINEAR)
# cv.imwrite(".\\resized-images\\001_bulbasaur.png", resized_image)
# cv.imshow("1", image)
# cv.imshow("2", resized_image)
# cv.waitKey(0)
