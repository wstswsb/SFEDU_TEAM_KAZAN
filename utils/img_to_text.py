import cv2
import pytesseract
from pytesseract import Output


class ImgToText:
    def translate(self, path_to_img: str) -> bytes:
        img = cv2.imread(path_to_img)
        text = pytesseract.image_to_string(
            img, lang="rus", output_type=Output.BYTES)
        return text
