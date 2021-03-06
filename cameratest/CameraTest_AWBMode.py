from picamera import PiCamera, Color
from time import sleep

# Modified from ch5listing5.py of Page 33 of TheMagPi 'Official Camera Guide' PDF

# NOTE: To make picamera preview show when viewing over VNC...
# Go to the VNC icon on the taskbar, click the Menu, Options > Troubleshooting
# and tick 'Enable Direct Capture Mode', and apply the changes

camera = PiCamera()
sleep(2) # allow the camera to start up fully

camera.start_preview(fullscreen=False, window = (50,150,1024,576))
for awbmode in camera.AWB_MODES:
    camera.awb_mode = awbmode
    camera.annotate_background = Color('black')
    camera.annotate_text = "AWB Mode : {0}".format(awbmode)
    camera.capture('/home/pi/Camera/img_awbmode_{0}.jpg'.format(awbmode))
    sleep(2)

camera.stop_preview()
camera.close() # to turn off the camera (and its Status LED) when the script has completed
