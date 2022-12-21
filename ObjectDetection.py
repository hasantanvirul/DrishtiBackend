import cv2
from PIL import Image
import numpy
from Mode import img

# OpenCV DNN
net = cv2.dnn.readNet('DrishtiApp/Object Detection/dnn_model/yolov4-tiny.weights', 'DrishtiApp/Object Detection/dnn_model/yolov4-tiny.cfg')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale=1/255)

# Load class lists
classes = []
with open("DrishtiApp/Object Detection/dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

img = cv2.imread(img)

# Object Detection
(class_ids, scores, bboxes) = model.detect(img);

# variables
count=0
result = ""

for class_id, score, bbox in zip(class_ids, scores, bboxes):
    (x, y, w, h) = bbox
    class_name = classes[class_id]
    count = count + 1
    cv2.putText(img, str(class_name), (x, y-10), cv2.QT_FONT_NORMAL, 1, (0,255,255), 1)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
    result = result + " " + class_name


print(result)

cv2.imshow("Output", img)
cv2.waitKey(0)

