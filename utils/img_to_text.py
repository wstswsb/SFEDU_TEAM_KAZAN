import cv2
import pytesseract


class ImgToText:
    def translate(self, img_path: str) -> str:
        img = cv2.imread("../images/4.jpg")
        text = pytesseract.image_to_string(img, lang="rus")
        return text
