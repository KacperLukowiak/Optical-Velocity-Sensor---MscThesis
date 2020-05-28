import time
import sys
import os
import picamera
import cv2
import numpy as np
import math
import glob


files = glob.glob('/var/tmp1/*')
for f in files:
    os.remove(f)

frames = 100

def initializeTemplateData():
    global y, x, h, w, angle_initial
    y = int(camera.resolution[0]/2) - 40
    x = int(camera.resolution[1]/2) - 40
    h = 80
    w = 80
    angle_initial = 0

def filenames():
    frame = 0
    while frame < frames:
        yield '/var/tmp1/image%02d.jpg' % frame
        if frame > 1:
            print('%d with %d' % (frame, frame-1))
            print('-----')
            # load images
            templatefullimage = cv2.imread('/var/tmp1/image%02d.jpg' % (frame-1))
            image = cv2.imread('/var/tmp1/image%02d.jpg' % (frame))
            # create a template
            template = templatefullimage[y:y + h, x:x + w].copy()
            # match the template with newer image
            cross_correlation_map = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
            # calculate max value of the cross-correlation map
            print('Max value of the cross-correlation matrix: %.12f' % (np.amax(cross_correlation_map)))
            # get coordinates of the max value
            max_coordinates = np.where(cross_correlation_map == np.amax(cross_correlation_map))
            print('Coordinates of the max value: %d , %d' % (max_coordinates[0], max_coordinates[1]))
            # calculate displacement
            displacement = [abs(y - max_coordinates[0]), abs(x - max_coordinates[1])]
            # calculate angle
            angle = angle_initial + math.atan2(y - max_coordinates[0], x - max_coordinates[1]) * 180 / np.pi
            print('Direction: %f degrees' % angle)
            print('Displacement: %d , %d' % (displacement[0], displacement[1]))

        if frame > 2:
            os.remove('/var/tmp1/image%02d.jpg' % (frame-2))
        frame += 1

with picamera.PiCamera() as camera:
    
    camera.resolution = (480, 270)
    initializeTemplateData()
    camera.framerate = 120
    time.sleep(2)
    start = time.time()
    camera.capture_sequence(filenames(), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
    frames,
    frames / (finish - start)))
    print('with time per one frame: %.12f' % ((finish-start)/frames))
    camera.close()
