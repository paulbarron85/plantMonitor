from picamera import PiCamera

camera = PiCamera()
#camera.vflip = True

camera.capture('image2.jpg')
