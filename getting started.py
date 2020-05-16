import cv2

img = cv2.imread('lena.jpg', 1)
print(img)

cv2.imshow('image',img)   # new img
k = cv2.waitKey(0)        # img waited for 10000 ms here

if k == 27:  # 27 represents escape key
    cv2.destroyAllWindows()   # closes img after 10000 ms
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()




