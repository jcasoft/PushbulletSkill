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

 
def get_image():
	retval, im = camera.read()
	return im


camera_port = 0
aplay_device = "plughw:1,0"

ramp_frames = 1
camera = cv2.VideoCapture(camera_port)

ws = create_connection("ws://localhost:8000/events/ws")
ws.send('{"message_type": "speak", "context": null, "metadata": {"utterance": "Say cheezzzzz"}}')

# You can change this time, depend your TTS respond
time.sleep(2)

for i in xrange(ramp_frames):
	temp = get_image()

os.system('aplay -D '+ aplay_device +' /opt/mycroft/third_party/mycroft-pushbullet-skill/script/camera-shutter-click-01.wav')

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


ws.send('{"message_type": "speak", "context": null, "metadata": {"utterance": "The picture is ready, and will be sent to your pushbullet account"}}')
result = ws.recv()
ws.close()
del(camera)
