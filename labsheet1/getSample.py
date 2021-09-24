import cv2
import os
import sys

cap = cv2.VideoCapture(sys.argv[1])
folder = os.path.dirname(os.path.realpath(__file__))

if not cap.isOpened():
    print('Can not open Video')

iteration = 0
idx = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        if(iteration == int(sys.argv[2])):
            title = "sample" + str(idx) + ".jpg"
            cv2.imwrite(folder + "/sample/" + title, frame)
            iteration = 0
            idx += 1
            print(folder + "/sample/" + title)
        else:
            iteration += 1
    else:
        break

cap.release()
cv2.destroyAllWindows()
