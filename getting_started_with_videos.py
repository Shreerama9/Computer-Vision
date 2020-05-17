import cv2

cap = cv2.VideoCapture(0)

forcc = cv2.VideoWriter_fourcc(*'XVID')          # 4CC codes
output = cv2.VideoWriter("HELO.avi",forcc,20.0,(640,480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        output.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
output.release()
cv2.destroyAllWindows()



