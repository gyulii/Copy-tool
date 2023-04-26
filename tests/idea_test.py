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


# https://stackoverflow.com/questions/64099248/pytesseract-improve-ocr-accuracy


tesseract_path = f"{os.path.abspath('.')}\\extensions\\tesseract\\tesseract.exe"


def main():
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    filename = "img.png"

    im = ImageGrab.grabclipboard()
    if im:
        im.save(f"{os.path.abspath('.')}\\tests\\img\\img.png", "PNG")

    image = cv2.imread(f"{os.path.abspath('.')}\\tests\\img\\img.png", 0)
    thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)[1]
    im = cv2.resize(image, None, fx=2, fy=2)
    cv2.imwrite(f"{os.path.abspath('.')}\\tests\\img\\img.png", im)

    config = "--oem 3 --psm %d" % 6
    txt = pytesseract.image_to_string(im, config=config, lang="deu")
    # txt = pytesseract.image_to_string(im, config = config, lang='eng')
    output = txt

    print(f"This is the original output: \n {output}")

    output = output.replace("—", "-")

    pyperclip.copy(output)
    with open(f"{os.path.abspath('.')}\\tests\\img\\solution.txt", "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    main()
