import numpy as np
import cv2
from find_obj import filter_matches,explore_match

img1 = cv2.imread('C:/Users/Charles/Dropbox/Projects/SUAS/2013 Competition/corrected/0.jpg') # queryImage
img2 = cv2.imread('C:/Users/Charles/Dropbox/Projects/SUAS/2013 Competition/corrected/1.jpg') # trainImage

img1 = cv2.cvtColor(img1, cv2.cv.CV_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.cv.CV_BGR2GRAY)

size1 = (int(img1.shape[1]*0.1), int(img1.shape[0]*0.1))
size2 = (int(img2.shape[1]*0.1), int(img2.shape[0]*0.1))

img1 = cv2.resize(img1, size1)
img2 = cv2.resize(img2, size2)

# Initiate SIFT detector
orb = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.

kp_pairs = []
for m in matches:
	kp_pairs.append([kp1[m.queryIdx], kp2[m.trainIdx]])

print kp_pairs
	
explore_match('find_obj', img1,img2,kp_pairs)#cv2 shows image
cv2.waitKey(0)