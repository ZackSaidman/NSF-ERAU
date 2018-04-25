import os
import re

import cv2
import latLonBound
import warp

path = 'Z:/Teams/SUAS/2015/Images5'

print path

files = [f for f in os.listdir(path) if f.endswith('.jpg')]

r = re.compile('.')

for f in files:
    num = re.split("\.", f)[0]
    print num
    im = cv2.imread(path + os.sep + num + '.jpg', 0)

    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY);

    f = open(path + os.sep + num + '.txt', 'r')
    line = f.readline()
    f.close()

    line = re.split("\t", line)[1]
    params = re.split(",", line)

    im = warp.flattenImage(im, float(params[3]), -1 * float(params[4]), float(params[5]))

    cv2.imwrite(path + os.sep + "corrected" + os.sep + num + ".png", im)

    points = latLonBound.getPoints(float(params[0]),
                                   float(params[1]),
                                   float(params[2]) * 0.3048,
                                   float(params[3]),
                                   float(params[4]),
                                   float(params[5]))

    f = open(path + os.sep + "corrected" + os.sep + num + ".txt", 'w')
    for point in points:
        f.write(str(point[0]) + "," + str(point[1]) + "\n")
    f.close()
raw_input()
