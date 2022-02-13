import cv2 as cv
  

#cv.imread method basically takes in an path to an image
#and returns that image to an matrix of pixels
#img = cv.imread("photos/lisa3.jpg")

#cv.imshow displays image as a new window
#cv.imshow("lisa3", img)
#Reading videos
capture = cv.VideoCapture("videos/lb.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows





#cv.waitKey(0)

