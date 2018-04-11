#!/usr/bin/env python
# Photo from Pushbullet Skill Script
# Author: Juan Carlos Argueta - JCASOFT

import sys

import time
import cv2

import os
from websocket import create_connection

from PIL import ImageEnhance
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import inspect

 
def get_image():
	retval, im = camera.read()
	return im


path_to_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

camera_port = 0
#aplay_device = "plughw:1,0"

ramp_frames = 1
camera = cv2.VideoCapture(camera_port)

SOUND_EFFECT = path_to_file + '/camera-shutter-click-01.wav'

ws = create_connection("ws://localhost:8181/core")

msg = 'Say cheez!'
ws.send('{"type": "speak", "data": {"utterance": "'+ msg +'"}, "context": null}')

# You can change this time, depend your TTS respond
time.sleep(4)

for i in xrange(ramp_frames):
	temp = get_image()

os.system('aplay ' +  SOUND_EFFECT)

camera_capture = get_image()

photo = '/tmp/photo.png'

cv2.imwrite(photo, camera_capture)


# Overlaying text over photo
font_fname = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
img = Image.open(photo)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_fname , 30)
draw.text((20, 20),"Photo from Mycroft",(255,255,255),font=font)
photo_out = '/tmp/photo.png'
img.save(photo_out)


msg = "The picture is ready, and will be sent to your pushbullet account!"
ws.send('{"type": "speak", "data": {"isDialog": null, "utterance": "'+ msg +'"}, "context": null}')

result = ws.recv()
ws.close()
del(camera)
