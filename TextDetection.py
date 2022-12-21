


from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigation
from Mode import img

"""# 2. Instantiate Model and Detect"""

# Setup model
ocr_model = PaddleOCR(lang='en')

# Run the ocr method on the ocr model
result = ocr_model.ocr(img)

result

for res in result:
    print(res[1][0])

