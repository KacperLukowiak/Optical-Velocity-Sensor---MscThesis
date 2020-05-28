import numpy as np
import sys
import cv2
import math
from timeit import default_timer as timer

np.set_printoptions(threshold=1000)
scale_percent = 25 # percent of original size

# load the images
img1 = cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image1.jpg', 0)
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)

img2 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image2.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img3 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image3.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img4 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image4.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img5 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image5.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img6 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image6.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img7 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image7.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img8 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image8.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img9 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image9.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img10 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles100microns\\image10.jpg', 0), dim, interpolation=cv2.INTER_AREA)

img1_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image1.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img2_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image2.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img3_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image3.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img4_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image4.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img5_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image5.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img6_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image6.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img7_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image7.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img8_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image8.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img9_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image9.jpg', 0), dim, interpolation=cv2.INTER_AREA)
img10_500 = cv2.resize(cv2.imread('C:\\Users\\kacpe\\Desktop\\Master Thesis\\picspeckles\\picspeckles500microns\\image10.jpg', 0), dim, interpolation=cv2.INTER_AREA)

lines = np.zeros((1080,1920,3), np.uint8)
cv2.imshow("xd", img1_500)


# set the coordinates of the template to the centre
y = int(img1.shape[0]/2) - 40
x = int(img1.shape[1]/2) - 40
h = 80
w = 80

# get the template
template = img1_500[y:y + h, x:x + w].copy()
c = 0
# images = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10]
stringi = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
images = [img1_500, img2_500, img3_500, img4_500, img5_500, img6_500, img7_500, img8_500, img9_500, img10_500]
angle_initial = 0

for img in images:
    start = timer()
    # match the template from previous image with a current image
    result = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
    # cv2.imshow(stringi[c], result)
    # find the peak
    print('Max value of the cross-correlation matrix: ', np.amax(result))
    # find the coordinates of the peak
    indexes = np.where(result == np.amax(result))
    print('Coordinates of the max value: ', indexes[0], indexes[1])
    # calculate displacement
    displacement = [abs(y - indexes[0]), abs(x - indexes[1])]
    angle = angle_initial + math.atan2(y - indexes[0], x - indexes[1]) * 180 / np.pi
    # cv2.line(lines, (x, y), (indexes[0], indexes[1]), (0, 255, 0), 3, 8, 0)
    # cv2.line(lines, (0, 0), (500, 500), (0, 255, 0), 3, 8, 0)
    print('Direction: ', angle, ' degrees')
    print('Displacement: ', displacement[0], displacement[1])
    # get template from the current image
    template = img[y:y + h, x:x + w].copy()
    end = timer()
    print(end - start)
    print('-----------------------------------------')
    c = c + 1

# cv2.imshow('path', lines)
cv2.waitKey()
cv2.destroyAllWindows()

