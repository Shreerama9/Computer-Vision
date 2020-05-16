import cv2

img = cv2.imread('lena.jpg', 1) # Here lena.jpg can be replaced by any of your imageor filename
print(img)

cv2.imshow('image',img)   
k = cv2.waitKey(0)        

if k == 27:  # 27 represents escape key
    cv2.destroyAllWindows()  
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()




