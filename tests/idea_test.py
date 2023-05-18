import os

import cv2
import numpy as np
import pyperclip
import pytesseract
from PIL import Image, ImageGrab

os.environ["PATH"] = f"{os.path.abspath('.')}\\extensions\\tesseract\\tesseract.exe"


def getText(filename):
    img = cv2.imread(filename)

    txt = pytesseract.image_to_string(img)
    return txt


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image


# https://stackoverflow.com/questions/64099248/pytesseract-improve-ocr-accuracy


tesseract_path = f"{os.path.abspath('.')}\\extensions\\tesseract\\tesseract.exe"


def main():
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    filename = "img.png"

    im = ImageGrab.grabclipboard()
    if im:
        im.save(f"{os.path.abspath('.')}\\tests\\img\\img.png", "PNG")

    image = cv2.imread(f"{os.path.abspath('.')}\\tests\\img\\img.png")
    gray_image = grayscale(image)

    # thick = thick_font(im_bw)
    image = cv2.resize(image, None, fx=3, fy=3)
    # thresh, im_bw = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f"{os.path.abspath('.')}\\tests\\img\\mod.png", image)

    config = "--oem 3 --psm 6"
    txt = pytesseract.image_to_string(image, config=config, lang="deu")
    # txt = pytesseract.image_to_string(im, config = config, lang='eng')
    output = txt

    print(f"This is the original output: \n {output}")

    output = output.replace("—", "-")
    output = output.replace("\”", '"')

    pyperclip.copy(output)
    with open(f"{os.path.abspath('.')}\\tests\\img\\solution.txt", "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    main()
