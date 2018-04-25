import os
import warp
import re
import cv2
import latLonBound

path = '2013 Competition'

print path

files = [ f for f in os.listdir(path) if f.endswith('.txt') ]

r = re.compile('.')

for f in files:
	num = re.split("\.", f)[0]
	print num

	f.close()
raw_input()