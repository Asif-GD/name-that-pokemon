# using opencv-python = "==4.5.5.62" because of autocomplete issues with PyCharm intellisense

import os
import sys
import cv2 as cv

# print(cv.__version__)

input_folder = sys.argv[1]
output_folder = sys.argv[2]

files_list = os.listdir(f".\\{input_folder}")

if not os.path.exists(f".\\{output_folder}"):
    os.mkdir(f".\\{output_folder}")

for file in files_list:
    image = cv.imread(f".\\{input_folder}{file}", cv.IMREAD_COLOR)
    only_file_name = os.path.splitext(file)[0]
    cv.imwrite(f".\\{output_folder}{only_file_name}.png", image)
