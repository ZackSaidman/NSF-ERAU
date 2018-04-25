import math

import cv2
import numpy as np


def flattenImage(im, psy, theta, phi):
    ySize, xSize = im.shape

    psy = math.pi * 2 - (psy + math.pi / 2)

    R = np.matrix([[math.cos(theta) * math.cos(psy),
                    math.cos(phi) * math.sin(psy) + math.sin(phi) * math.sin(theta) * math.cos(psy),
                    math.sin(phi) * math.sin(psy) - math.cos(phi) * math.sin(theta) * math.cos(psy)],
                   [-1 * math.cos(theta) * math.sin(psy),
                    math.cos(phi) * math.cos(psy) - math.sin(phi) * math.sin(theta) * math.sin(psy),
                    math.sin(phi) * math.cos(psy) + math.cos(phi) * math.sin(theta) * math.sin(psy)],
                   [math.sin(theta), -1 * math.sin(phi) * math.cos(theta), math.cos(phi) * math.cos(theta)]],
                  dtype='float32')

    p = np.matrix([[-0.5, 0.5, 1],
                   [0.5, 0.5, 1],
                   [0.5, -0.5, 1],
                   [-0.5, -0.5, 1]], dtype='float32')

    newPts = []
    for i in p:
        v = R * np.transpose(i)
        newPts.append(v / v[2])

    xOffset = float("inf")
    yOffset = float("inf")
    for i in newPts:
        x = i.item(0)
        y = i.item(1)
        if x < xOffset:
            xOffset = x
        if y < yOffset:
            yOffset = y

    dst = np.empty([4, 2], np.float32)
    xMax = float("-inf")
    yMax = float("-inf")
    for i in range(len(newPts)):
        dst[i][0] = (newPts[i].item(0) - xOffset) * xSize
        dst[i][1] = (newPts[i].item(1) - yOffset) * ySize
        if dst[i][0] > xMax:
            xMax = dst[i][0]
        if dst[i][1] > yMax:
            yMax = dst[i][1]

    src = np.array([[0, ySize], [xSize, ySize], [xSize, 0], [0, 0]], np.float32)

    m = cv2.getPerspectiveTransform(src, dst)
    try:
        im = cv2.warpPerspective(im, m, (xMax, yMax), im, cv2.INTER_NEAREST, cv2.BORDER_CONSTANT)
    except:
        pass
    return im
