
import time
from os.path import dirname, join, expanduser
import os


from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message

from mycroft.util import record, play_wav
from os.path import dirname, join
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from pushbullet import Pushbullet
import subprocess
import inspect



__author__ = 'jcasoft'


LOGGER = getLogger(__name__)
 
path_to_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))



class PushbulletSkill(MycroftSkill):
    """
    A Skill to send message using Pushbullet
    """
 

    def __init__(self):
        super(PushbulletSkill, self).__init__(name="PushbulletSkill")

	self.audio_effects = "/opt/mycroft/skills/PushbulletSkill/"
	self.enable_fallback = False
        self._setup()
        try:
            self.settings.set_changed_callback(self._force_setup)
        except BaseException:
            LOGGER.debug(
                'No auto-update on changed settings (Outdated version)')

        try:
            self.settings.set_changed_callback(self._force_setup)
        except BaseException:
            LOGGER.debug(
                'No auto-update on changed settings (Outdated version)')




    def _setup(self, force=False):
        if self.settings is not None:
             self.api_key = self.settings.get('api_key')
            

	self.photo_script = "/opt/mycroft/skills/PushbulletSkill/script/photo.py"
	self.photo_img = "/tmp/photo.png"
	self.help_audio = "/tmp/help"

	"""
	Register Mycroft device to Pushbullet
	"""
	self.pb = Pushbullet(self.api_key)
	"""
	Get the contacts list from Pushbullet Mycroft device registered
	"""
	self.contactspb = self.pb.chats
	self.devicespb = self.pb.devices

	self.contacts={}
	for i in range(len(self.contactspb)):	
	    row_contact = str(self.contactspb[i])
	    name = row_contact.split("'",1)[1].split("'")[0]
	    name = name.replace(" ","").lower()
	    email = row_contact.split("<",1)[1].split(">")[0]
	    self.contacts[name] = self.contactspb[i]

	self.devices={}
	for i in range(len(self.devicespb)):	
	    row_device = str(self.devicespb[i])
	    name = row_device.split("'",1)[1].split("'")[0]
	    name = name.replace(" ","").lower()
	    self.devices[name] = self.devicespb[i]

    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.load_regex_files(join(dirname(__file__), 'regex', self.lang))

        intent = IntentBuilder("PushMessageIntent")\
        	.require("PushMessageKeyword")\
		.require("Contact")\
		.require("Message")\
		.build()
        self.register_intent(intent, self.handle_pushmessage)

        intent = IntentBuilder("PushMeMessageIntent")\
        	.require("PushMessageKeyword")\
		.require("MeKeyword")\
		.require("SelfMessage")\
		.build()
        self.register_intent(intent, self.handle_push_me_message)

        intent = IntentBuilder("PushPhotoIntent")\
		.require("PushPhotoKeyword")\
		.build()
        self.register_intent(intent, self.handle_pushphoto)

        intent = IntentBuilder("PushHelpIntent")\
		.require("PushHelpKeyword")\
		.build()
        self.register_intent(intent, self.handle_help)

    def handle_pushmessage(self, message):
        try:
            contact = message.data.get("Contact").lower()
            if contact in self.contacts:
		"""
    		Evaluate a exact contact to send message using Pushbullet
    		"""
                chat = self.contacts.get(contact)
                msg = message.data.get("Message")
	   	push = self.pb.push_note("Message from Mycroft",msg, chat=chat)
	   	data = {"contact": contact}
	   	self.speak_dialog("push.message",data)
            elif contact in self.devices:
		"""
    		Evaluate a exact device to send message using Pushbullet
    		"""
                device = self.devices.get(contact)
                msg = message.data.get("Message")
	   	push = self.pb.push_note("Message from Mycroft",msg, device=device)
	   	data = {"contact": contact}
	   	self.speak_dialog("push.device",data)
	    else:
		"""
    		Evaluate a similar contact to send message using Pushbullet
    		"""
		matching_contact = [s for s in self.contacts if contact in s]
		matching_device = [d for d in self.devices if contact in d]

		matching_contact = str(matching_contact)
		matching_device = str(matching_device)

		if len(matching_contact) > 2:
			name_match = matching_contact.split("'",1)[1].split("'")[0]
			chat = self.contacts.get(name_match)
	                msg = message.data.get("Message")
		   	push = self.pb.push_note("Message from Mycroft",msg, chat=chat)
		   	data = {"contact": name_match}
		   	self.speak_dialog("push.message",data)
		elif len(matching_device) > 2:
			name_match = matching_device.split("'",1)[1].split("'")[0]
			device = self.devices.get(name_match)
	                msg = message.data.get("Message")
			full_name = str(device).split("'")
			full_name = full_name[1]
		   	push = self.pb.push_note("Message from Mycroft",msg, device=device)
		   	data = {"contact": full_name}
		   	self.speak_dialog("push.device",data)

        except Exception as e:
	    data = {"contact": contact}
	    self.speak_dialog("processing.pushmessage",data)


    def handle_push_me_message(self, message):

	msg = message.data.get("SelfMessage")
   	push = self.pb.push_note("Message from Mycroft",msg)
   	self.speak_dialog("push.self.message")


    def	handle_pushphoto(self, message):
	"""
	Run photo_cmd (photo.py) outside Mycroft Virtual Environment 
    	"""
	photo_cmd = "/usr/bin/python2.7 " + self.photo_script
	os.system(photo_cmd)

	time.sleep(1)
	with open(self.photo_img,"rb") as png:
	    file_data = self.pb.upload_file(png, "photo.png")
        #chat = self.chat
  	push = self.pb.push_file(**file_data)


    def	handle_help(self, message):
	"""
	Record 10 seconds to help_audio_file.mp3 file
    	"""
	self.speak_dialog("push.help")
	time.sleep(7)
	p = play_wav(self.audio_effects+"ding.wav")
	p.communicate()


	r = record(self.help_audio+".wav",10,16000,1)
	r.communicate()

	p = play_wav(self.audio_effects+"dong.wav")
	p.communicate()

	with open(self.help_audio+".wav","rb") as mp3:
	    file_data = self.pb.upload_file(mp3, "help_audio_file.wav")
	chat = self.pb.devices
  	push = self.pb.push_file(**file_data)
	self.speak_dialog("push.help.send")

	
    def stop(self):
        pass

def create_skill():
    return PushbulletSkill()
