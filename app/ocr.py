import os

import cv2
import numpy as np
import pyperclip
import pytesseract
from PIL import Image, ImageGrab



def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)





class OCR_engine_interface:
    def __init__(self , input_language : str ="deu", auto_copy_to_clipboard : bool = True , engine_enabled : bool = True):
        self.input_language = input_language
        self.auto_copy_to_clipboard = auto_copy_to_clipboard
        self.engine_enabled = engine_enabled
        
        self.tesseract_path = f"{os.path.abspath('.')}\\extensions\\tesseract\\tesseract.exe"
        os.environ["PATH"] = f"{os.path.abspath('.')}\\extensions\\tesseract\\tesseract.exe"


    def image_to_text(self) -> str:
        if self.engine_enabled is False:
            return f"Engine disabled, if you wish to use it please enable it"
        else:
            pytesseract.pytesseract.tesseract_cmd = self.tesseract_path
            image_PIL = ImageGrab.grabclipboard()
            if image_PIL:
                image_PIL.save(f"{os.path.abspath('.')}\\app\\img\\placeholder.png", "PNG")
                
            image_raw =cv2.imread(f"{os.path.abspath('.')}\\app\\img\\placeholder.png")

            image_gray = grayscale(image_raw)

            #thick = thick_font(im_bw)
            image_scaled = cv2.resize(image_gray, None, fx=3, fy=3)
            #thresh, im_bw = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
            

            config = "--oem 3 --psm 6"
            txt_raw = pytesseract.image_to_string(image_scaled, config=config, lang=self.input_language)
            # txt = pytesseract.image_to_string(im, config = config, lang='eng')
            output_text = txt_raw


            output_text = output_text.replace("—", "-")
            output_text = output_text.replace("\”", "\"")
            print(output_text)
            if self.auto_copy_to_clipboard is True:
                pyperclip.copy(output_text)
            return output_text
        


if __name__ == "__main__":
    OCR_Engine = OCR_engine_interface()
    OCR_Engine.image_to_text()
    
    

