import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
import os
import re
import latLonBound


imgOriginal = cv2.imread('Untitled.png', 1)

top = 38.154689
bottom = 38.14076
left = -76.442947
right = -76.409360

w = 1090
h = 610

def drawPoint(img, p, color=cv2.cv.Scalar( 0, 0, 255 )):
	cv2.circle( img,
			 p,
			 5,
			 color,
			 -1,
			 8 );

def doPlot(lat, lon, alt, roll, pitch, yaw):
	img = imgOriginal.copy()
	points = latLonBound.getPoints(	lat, 
										lon, 
										alt, 
										roll,
										pitch, 
										yaw)

	#determine points on image
	degreesPPV = (top - bottom) / h
	degreesPPH = (left - right) / w

	f = open('asdf.txt', 'w')
	for point in points:
		f.write(str(point[0]) + "," + str(point[1]) + "\n" )
		
		y = (top - point[0]) / degreesPPV
		x = (left - point[1]) / degreesPPH
		
		drawPoint(img, (int(x), int(y)))
	f.close()

	#plot bird
	y = (top - lat) / degreesPPV
	x = (left - lon) / degreesPPH
	drawPoint(img, (int(x), int(y)), cv2.cv.Scalar( 255, 0, 0 ))

	cv2.imshow('image',img)
	cv2.waitKey(0)

if __name__ == 'asdf':	
	path = r"C:\Users\Chuck\Desktop\2015 Competition"
	num = 47
	f = open(path + os.sep + str(num) + '.txt', 'r')
	line = f.readline()
	f.close()

	line = re.split("\t", line)[1]
	params = re.split(",", line)	

	real = False
	if real:
		lat = float(params[0])
		lon = float(params[1])
		alt = (float(params[2])+90) * 0.3048
		roll = float(params[4])
		pitch = float(params[5])
		yaw = float(params[3])
	else:
		lat = 38.1426192
		lon = -76.4335276
		alt = 61.5 * 0.3048
		roll = 38.18 * math.pi/180.0
		pitch = -1.19 * math.pi/180.0
		yaw = 182.96 * math.pi/180.0
	
	doPlot(lat, lon, alt, roll, pitch, yaw)
	cv2.destroyAllWindows()	
	
	
	
	
if __name__ == '__main__':
	f = open('FifteenDataSlow.csv', 'r')
	for line in f:
		params = line.split(',')
		print params
		doPlot(float(params[1]), 
		float(params[2]), 
		float(params[3]), 
		-1*float(params[4]) * math.pi/180.0, 
		float(params[5]) * math.pi/180.0, 
		float(params[6]) * math.pi/180.0)