import numpy as np
import cv2
import math
from find_obj import filter_matches,explore_match

MIN_MATCH_COUNT = 10

im1 = cv2.imread('C:/Users/Charles/Dropbox/Projects/SUAS/2013 Competition/corrected/0.jpg') # queryImage
im2 = cv2.imread('C:/Users/Charles/Dropbox/Projects/SUAS/2013 Competition/corrected/1.jpg') # trainImage

img1 = cv2.cvtColor(im1, cv2.cv.CV_BGR2GRAY)
img2 = cv2.cvtColor(im2, cv2.cv.CV_BGR2GRAY)

size1 = (int(img1.shape[1]*0.1), int(img1.shape[0]*0.1))
size2 = (int(img2.shape[1]*0.1), int(img2.shape[0]*0.1))

img1 = cv2.resize(img1, size1)
img2 = cv2.resize(img2, size2)

# Initiate SIFT detector
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

dist = []
for (m,n) in matches:
	#f.write(''.join('%s\t' % x for x in kp1[m.queryIdx].pt))
	#f.write(''.join('%s\t' % x for x in kp2[m.trainIdx].pt) + '\n')
	p1 = kp1[m.queryIdx].pt
	p2 = kp2[m.trainIdx].pt
	dist.append(math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2)))

avgDist = sum(dist)/float(len(dist))

query = []
train = []
idx = 0
goodMatches = []
for d in dist:
	if ((d > avgDist-(avgDist*0.15)) and d < avgDist+(avgDist*0.15)):
		goodMatches.append(matches[idx])
		query.append(kp1[matches[idx][0].queryIdx].pt)
		train.append(kp2[matches[idx][0].trainIdx].pt)
	idx = idx + 1

query = np.asarray(query)/0.1
train = np.asarray(train)/0.1

m = cv2.findHomography(query, train, cv2.RANSAC,5.0)[0]
img3 = cv2.warpPerspective(im1, m, (im1.shape[1], im1.shape[0]))

p1, p2, kp_pairs = filter_matches(kp1, kp2, goodMatches)
explore_match('find_obj', img1,img2,kp_pairs)#cv2 shows image

cv2.imwrite('asdf.jpg', img3)
cv2.waitKey(0)
