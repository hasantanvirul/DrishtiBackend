# This program prints Hello, world!
import FlaskAPI
import ObjectDetection
import TextDetection
import CurrencyDetection

# mode= app.img
def testing(mode, img):
    if mode=="0":
        class_text="Mode doesn't exist"
    elif mode=="1":
            class_text=ObjectDetection.result
    elif mode=="2":
        class_text=TextDetection.result
    elif mode=="3":
        class_text=CurrencyDetection.class_name
    elif mode=="4":
        class_text=TextDetection.result
    else:
        class_text="Wrong Mode Chosen"

    return class_text

# print('Hello, world!')