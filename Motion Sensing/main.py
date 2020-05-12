import cv2 as cv

# dataset = cv.VideoCapture('dataset_video.mp4')                          # When using an already captured video as dataset
dataset = cv.VideoCapture(0)                                               # Uses Camera No.0 to take input , change accordingly on no. of camera you got.

subtractor = cv.createBackgroundSubtractorMOG2(history=200, varThreshold=50)

while True:

    ret, frame = dataset.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        if cv.waitKey(delay=5) == ord('x'):                                # Terminates Script when pressed X
            break

#    else:
#        dataset = cv.VideoCapture('dataset_video.mp4')                   // You have to re-iterate when performing on a pre-captured video

cv.destroyAllWindows()
dataset.release()
