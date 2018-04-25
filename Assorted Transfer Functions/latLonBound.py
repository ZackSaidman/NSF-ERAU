import numpy as np
import math

#radius of the earth in meters
r_earth = 6371000

def getCorners(hfov=69.0, vfov=49.6):#Field of view on camera
	
	points = []
	
	hfov = hfov*math.pi/180
	vfov = vfov*math.pi/180
	
	#upper left
	points.append(np.matrix	([	
								[math.tan(vfov/2)],
								[math.tan(hfov/2)],
								[1]
							]))
	#lower left
	points.append(np.matrix	([	
								[-1*math.tan(vfov/2)],
								[math.tan(hfov/2)],
								[1]
							]))
	#lower right
	points.append(np.matrix	([	
								[-1*math.tan(vfov/2)],
								[-1*math.tan(hfov/2)],
								[1]
							]))
	#upper right
	points.append(np.matrix	([	
								[math.tan(vfov/2)],
								[-1*math.tan(hfov/2)],
								[1]
							]))
	
	return points

#angles in radians please

def rotateVector(vector, phi, theta, psi):
	
	#print phi, theta, psi
	
	R = np.matrix([	[	math.cos(phi),		0.0,		math.sin(phi)	],
					[	0.0,					1.0,		0.0				],
					[	-1*math.sin(phi),	0.0,		math.cos(phi)	]		])
	
	P = np.matrix([	[	1.0,		0.0,						0.0],
					[	0.0,		math.cos(theta),		math.sin(theta)],
					[	0.0,		-1*math.sin(theta), 	math.cos(theta)]	])
	
	Y = np.matrix([	[	math.cos(psi),		math.sin(psi),			0.0],
					[	-1*math.sin(psi),	math.cos(psi),		0.0],
					[	0.0,					0.0, 						1.0]	])
	
	a = R*vector
	#print a
	b = P*a
	#print b
	c = Y*b
	#print c
	return c

def projectToGround(vector, lat, lon, alt):
	#normalize the vector so that z = 1
	vector = vector/vector.item(2)
	#project the vector to the ground level, alt should be AGL not MSL.
	vector = vector*alt
	newLat  = lat  + (vector.item(1) / r_earth) * (180.0 / math.pi)
	newLon = lon + (vector.item(0) / r_earth) * (180.0 / math.pi) / math.cos(lat * math.pi/180.0)
	
	return [newLat, newLon]

def getPoints(lat, lon, alt, roll, pitch, yaw):
	corners = getCorners()
	
	points = []
	for corner in corners:
		corner = rotateVector(corner, roll, pitch, yaw)
		point = projectToGround(corner, lat ,lon, alt)
		points.append(point)
	return points
		
if __name__ == "__main__":
	
	vector = np.matrix([[0], [0], [1]])
	
	roll = -10.0
	pitch = 10.0
	yaw = 90.0
		
	lat = 38.145756
	lon = -76.427127
	alt = 100.0	
	
	f = open('asdf.txt', 'w')
	p = getPoints(lat,lon,alt,roll, pitch, yaw)
	for point in p:
		f.write(str(point[0]) + "," + str(point[1]) + "\n" )
	f.close()
	