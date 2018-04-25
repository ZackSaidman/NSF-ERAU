top = 38.156100
bottom = 38.137061
left = -76.441898
right = -76.415675

w = 1039
h = 634

#determine points on image
vDelta = (top - bottom)
hDelta = (left - right)
degreesPPV = vDelta / h
degreesPPH = hDelta / w

y = (top - (bottom + vDelta/4)) / degreesPPV
x = (left - (right + hDelta/2)) / degreesPPH

print x, y