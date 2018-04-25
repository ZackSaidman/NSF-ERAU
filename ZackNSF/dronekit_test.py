#Brian was here :)

from dronekit import connect
import time
import socket
v = connect('/dev/serial/by-id/usb-3D_Robotics_PX4_BL_FMU_v2.x_0-if00', wait_ready=True, baud=9600)
print v

while 1:
##    print v.location.global_frame
    print v.attitude
    time.sleep(1)
