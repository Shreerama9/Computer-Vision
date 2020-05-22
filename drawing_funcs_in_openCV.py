import numpy as np
import cv2

# img = cv2.imread('lena.jpg', -1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (175, 200, 60), 7)   # BGR
img = cv2.arrowedLine(img, (70, 30), (255, 255), (175, 0, 60), 7)
img = cv2.rectangle(img, (200, 100), (400, 455), (255, 0, 0), 5)  # when thickness is used as -1 it will fill itself

img = cv2.circle(img, (100,200), 20, (20, 255, 22), -1 )
# TRY POLYGONS AND ELIPSE


font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Learning', (10,40),font, 2, (25, 40, 69), 2, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()