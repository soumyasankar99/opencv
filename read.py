import cv2 as cv

"""img = cv.imread('images/cat-1.jpg')

cv.imshow('Cat' ,img)"""

#reading videos
capture = cv.VideoCapture('video\pexels-magda-ehlers-3040808-3840x2160-30fps.mp4')

while True:
    isTrue , frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release ()  
cv.destroyAllWindows()    
