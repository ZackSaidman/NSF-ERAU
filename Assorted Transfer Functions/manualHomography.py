import numpy as np
import cv2
import math
from find_obj import filter_matches,explore_match

img1 = cv2.imread('C:/Users/Charles/Dropbox/Projects/SUAS/2013 Competition/corrected/0.jpg') # queryImage

src = np.array([[3761.0,1929.0],[4553.0,2825.0],[7065.0,3849.0]], 'float32') #,(5713,4521)])
dst = np.array([[565.0,2189.0],[941.0,2805.0],[2353.0,3529.0]], 'float32') #,(1469,3937)])

print src
print dst

m = cv2.getAffineTransform(src,dst) #findHomography(src, dst, cv2.RANSAC,5.0)[0]
print m
img3 = cv2.warpAffine(img1, m, (img1.shape[1], img1.shape[0]))

cv2.imwrite('asdf.jpg', img3)
