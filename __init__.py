# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.



import time
from os.path import dirname, join
import os


from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message

from mycroft.util import record, play_wav
from os.path import dirname, join
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from pushbullet import Pushbullet
#from websocket import create_connection


__author__ = 'jcasoft'


LOGGER = getLogger(__name__)


class PushbulletSkill(MycroftSkill):
    """
    A Skill to send message using Pushbullet
    """
 

    def __init__(self):
        super(PushbulletSkill, self).__init__(name="PushbulletSkill")

        self.api_key = self.config.get('api_key')
	self.contact = ''
	self.chat = ''
	self.photo_script = self.config.get('photo')
	self.photo_img = self.config.get('photo_img')

	"""
	Register Mycroft device to Pushbullet
	"""
	self.pb = Pushbullet(self.api_key)
	"""
	Get the contacts list from Pushbullet Mycroft device registered
	"""
	self.contactspb = self.pb.chats
	
	self.contacts={}
	for i in range(len(self.contactspb)):	
	    row_contact = str(self.contactspb[i])
	    name = row_contact.split("'",1)[1].split("'")[0]
	    name = name.replace(" ","").lower()
	    email = row_contact.split("<",1)[1].split(">")[0]
	    self.contacts[name] = self.contactspb[i]


    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.load_regex_files(join(dirname(__file__), 'regex', self.lang))


        pushmessage_intent = IntentBuilder("PushMessageIntent").\
            require("PushMessageKeyword").require("Contact").require("Message").build()
        self.register_intent(pushmessage_intent, self.handle_pushmessage)

        pushphoto_intent = IntentBuilder("PushPhotoSkillIntent").require(
            "PushPhotoStartKeyword").build()
        self.register_intent(pushphoto_intent, self.handle_pushphoto)

    def handle_pushmessage(self, message):
        try:
            contact = message.metadata.get("Contact").lower()
            if contact in self.contacts:
		"""
    		Evaluate a exact contact to send message using Pushbullet
    		"""
                chat = self.contacts.get(contact)
                msg = message.metadata.get("Message")
	   	push = self.pb.push_note("Message from Mycroft",msg, chat=chat)
	   	data = {"contact": contact}
	   	self.speak_dialog("pushmessage",data)
	    else:
		"""
    		Evaluate a similar contact to send message using Pushbullet
    		"""
		matching = [s for s in self.contacts if contact in s]
		matching = str(matching)
		name_match = matching.split("'",1)[1].split("'")[0]
		chat = self.contacts.get(name_match)
                msg = message.metadata.get("Message")
	   	push = self.pb.push_note("Message from Mycroft",msg, chat=chat)
	   	data = {"contact": name_match}
	   	self.speak_dialog("pushmessage",data)

        except Exception as e:
	    data = {"contact": contact}
	    self.speak_dialog("processing.pushmessage",data)


    def	handle_pushphoto(self, message):
	"""
	Run photo_cmd (photo.py) outside Mycroft Virtual Environment 
    	"""
	photo_cmd = "/usr/bin/python2.7 " + self.photo_script
	os.system(photo_cmd)

	time.sleep(1)
	with open(self.photo_img,"rb") as png:
	    file_data = self.pb.upload_file(png, "Photo from Mycroft")
        chat = self.chat
  	push = self.pb.push_file(**file_data)
	
    def stop(self):
        pass

def create_skill():
    return PushbulletSkill()