# import cv2

# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         break
# cv2.destroyWindow("preview")

import time
import cv2
camera_port = 0

cv2.namedWindow("preview")
camera = cv2.VideoCapture(camera_port)

if camera.isOpened(): # try to get the first frame
    rval, frame = camera.read()
else:
    rval = False

# time.sleep(0.1)  # If you don't wait, the image will be dark

while rval:
    cv2.imshow("preview", frame)
    rval, frame = camera.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        return_value, image = camera.read()
        print(image)
        cv2.imwrite("opencv.jpg", image)
        break
cv2.destroyWindow("preview")
del(camera)  # so that others can use the camera as soon as possible