**PushbulletSkill**
===================

For Mycroft with new API (https://home.mycroft.ai) 
An skill to use with Mycroft that allows you to send messages, 10 seconds audio file and photos using **Pushbullet**
New features: message to self account and help audio file to devices

This uses  [pushbullet.py](https://pypi.python.org/packages/7d/a8/7fbed382824e84a51dfdc13315d9171fb6dc0670803ccb400931b9e3465b/pushbullet.py-0.10.0.tar.gz#md5=24db6917a12e1c9b3fecca102615376b)


----------

Prerequisites for Photo feature
-------------
You must have installed this only if use a photo feature:
> - **OpenCV** You can use this [link](http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/)  as a reference or search other
> - Python **PIL** , for install :  `pip install Pillow` 


Prerequisites for Pushbullet
-------------
Download pushbullet.py-0.10.0.tar.gz from link listed  **above**

> **Note:**

> - Install audio convert tool

     sudo apt-get install lame


> - Download pushbullet

     tar -xvzf pushbullet.py-0.10.0.tar.gz
     cd pushbullet.py-0.10.0

> - Now install pushbullet inside Mycroft virtual environment, for that do the following

     workon mycroft
     python setup.py install


- Create your account on  [pushbullet.com](https://www.pushbullet.com/) to get your [Access Token](https://www.pushbullet.com/#settings)
- Install pushbullet on your phone 
- Make some contacts



----------


Installation
-------------------
**Clone PushbulletSkill repository** on third party skill directory

    cd  $HOME/.mycroft/skills

    git clone  https://github.com/jcasoft/PushbulletSkill.git

<i class="icon-cog"></i>Add 'PushbulletSkill' section in your Mycroft configuration file on: 

    $HOME/.mycroft/mycroft.conf

	"PushbulletSkill": {
		"api_key": "o.XXXXXXXXXX",  	# <-- Replace with your Access token,
		"plughw": 0  			# <-- Audio Output index device 
	}



Restart Skills

    ./start.sh skills


----------


Features
--------------------

Currently this skill can do the following things (with some variation):

- push juancarlos barcelona is the best soccer team of the world
- photo
- push me remember to see the walking dead
- help "i had an accident and i need help" in audio file (not text)

> **Note:**
> - push - to invoke a push message to a contact
> - juancarlos - is the name of a contact that must exist in your pushbullet account, you can to pronounce the name or a part of the name from the beginning, if there is no contact, mycroft say a message that the contact not exist.
> - barcelona is the best soccer team of the world - is the message

> **Note:**
> - photo - to invoke a push photo to your own pushbullet account
> - The photo is sent to your pushbullet account

> **Note:**
> - push me - to invoke a push message to your own pushbullet account
> - The photo is sent to your pushbullet account

> **Note:**
> - help - to invoke a push 10 seconds audio file to your own pushbullet account
> - The audio file is sent to your devices associated to your pushbullet account


**Enjoy !**
--------

