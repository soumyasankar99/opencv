import cv2 as cv

img = cv.imread('images/cat-1.jpg')

cv.imshow('Cat' ,img)

def rescaledFrame(frame, scale=0.30):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaledFrame(img)
cv.imshow('Image',resized_image)
cv.waitKey(0)


#Reading videos
capture = cv.VideoCapture('video\pexels-magda-ehlers-3040808-3840x2160-30fps.mp4')

while True:
    isTrue , frame = capture.read()

    frame_resized = rescaledFrame(frame,scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release ()  
cv.destroyAllWindows()     



