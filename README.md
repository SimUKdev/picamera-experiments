# Picamera Experiments

This repo contains some examples from my experiments with the Picamera python module on a Raspberry Pi. I have tested it with a 5MP V1 and 8MP V2 camera module, but it should also work with the 12MP Raspberry Pi HQ camera.

For many of these tests I've created a `Camera` directory at `/home/pi/Camera/` which contains my files, and is the location where the photos and video files are saved to, but this can be adjusted in the code as appropriate.

### Picamera preview when using VNC
Note: When using VNC to access a Raspberry Pi remotely, instead of directly connected to a monitor, the Picamera preview window will not display unless you make a small settings change:
* go to the 'VNC' icon on the Raspberry Pi OS taskbar
* click the Menu, Options > Troubleshooting
* and tick 'Enable Direct Capture Mode', and apply the changes

#### Repo Contents

* `cameratest` contains some Python 3 scripts which I've used to test Raspberry Pi camera modules with Picamera, and currently includes some simple previews of the different Effects and Automatic White Balance modes, with each variation being saved as a separately named jpg file.

### Documentation
There are various sources of informaiton to learn more about the Raspberry Pi camera module and the Picamera python library. These are some I found useful:

* Documentation for the PiCamera python module is available at https://picamera.readthedocs.io/
* Official documentation for the Camera modules is available from Raspberry Pi's website https://www.raspberrypi.org/documentation/hardware/camera/README.md
* Official Raspberry Pi Camera Guide book https://magpi.raspberrypi.org/books/camera-guide