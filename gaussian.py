import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.createTrackbar('gaussian','image',1,100,nothing)

while(True):
    ret, frame = cap.read()

    gaussian = cv2.getTrackbarPos('gaussian','image')

    g_frame = cv2.GaussianBlur(frame, (15, 15), gaussian/10)

    cv2.imshow('image', g_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
