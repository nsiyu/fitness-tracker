import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('Camera cannot open')
    exit()
while True:
    ret,frame = cap.read()
    #frame = cv.flip(frame, 0)
    if not ret:
        print('Cannot recieve frame')
        break
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break