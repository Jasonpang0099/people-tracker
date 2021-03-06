# coding:utf-8

import numpy as np
import cv2
import imutils

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh


def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness)



if __name__ == '__main__':
    import sys
    from glob import glob
    import itertools as it

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image = cv2.imread('faces.jpg')
    img = imutils.resize(image, width=min(400, image.shape[1]))
    print img, type(img)
    found, weights = hog.detectMultiScale(img, winStride=(8, 8), padding=(16, 16), scale=1.05)
    print found, type(found)
    draw_detections(img, found)
    # draw_detections(img, found_filtered, 3)
    cv2.imshow('img', img)
    ch = cv2.waitKey(0)
    cv2.destroyAllWindows()