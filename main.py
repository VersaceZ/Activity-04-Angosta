import cv2 as cv
filePath='Balls.jpg'
windowTitle = 'Balls'
readCvImage = cv.imread(filePath, 1)
cv.imshow(windowTitle, readCvImage)
cv.waitKey(0)
cv.destroyAllWindows()