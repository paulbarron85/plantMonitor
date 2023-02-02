import sys
import os
import datetime
import time
import argparse
import pause

parser=argparse.ArgumentParser()
parser.add_argument("captureTime",type=int,help='length of capture (hours)')
parser.add_argument("captureInterval",type=int,help='number of images to take (seconds)')
parser.add_argument("--startTime")
args=parser.parse_args()

FPS_IN = 20
FPS_OUT = 30

numCaptureFrames=(args.captureTime)*3600/(args.captureInterval)
filmLength=numCaptureFrames/FPS_IN

print('Capture time {} hours (user input arg)'.format(args.captureTime))
print('Capture interval {} seconds (user input arg)'.format(args.captureInterval))
print('Number of capture frames {0:.0f} (calculated)'.format(numCaptureFrames))
print('Final film FPS_IN {} (hardcoded)'.format(FPS_IN))
print('Final film FPS_OUT {} (hardcoded)'.format(FPS_OUT))
print('Final film length {} seconds (calculated)'.format(filmLength))

try:
    start = datetime.datetime.strptime(args.startTime,("%y%m%d%H%M"))
    print(start)
except:
    print("Time not in YYMMDDHHMM format")
    sys.exit(1)
print("Waiting until {}".format(start))
pause.until(start)

dirPath='{:%Y-%m-%d_%H:%M}'.format(datetime.datetime.now())
print("Creating folder {}".format(dirPath))
os.makedirs(dirPath)

print('To escape loop, use Ctrl+C')
frameCount = 0
while frameCount < numCaptureFrames:
    imageNumber = str(frameCount).zfill(7)
    print('Taking image {}'.format(imageNumber))
    os.system("raspistill -o %s/image%s.jpg"%(dirPath,imageNumber))
    frameCount += 1
    time.sleep(args.captureInterval - 6) #Takes roughly 6 seconds to take a picture

print("Converting images to video")
#os.system("avconv -r %s -i images/image%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=2592:1458,scale=1280:720 timelapse.mp4"%(FPS_IN,'%7d',FPS_OUT))
os.system("ffmpeg -y -framerate {} -pattern_type glob -i '{}/*.jpg' -c:v libx264 -r {} -vf scale=iw*.5:-1 -pix_fmt yuv420p {}/timelapse{}.mp4".format(FPS_IN,dirPath,FPS_OUT,dirPath,dirPath))
