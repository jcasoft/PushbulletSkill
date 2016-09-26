**PushbulletSkill**
===================


An skill to use with Mycroft that allows you to send messages and photos using **Pushbullet**

This uses  [pushbullet.py](https://pypi.python.org/packages/7d/a8/7fbed382824e84a51dfdc13315d9171fb6dc0670803ccb400931b9e3465b/pushbullet.py-0.10.0.tar.gz#md5=24db6917a12e1c9b3fecca102615376b)


----------

Prerequisites
-------------
You must have installed:
> - **OpenCV** You can use this [link](http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/)  as a reference or search other
> - Python **PIL** , for install :  `pip install Pillow` 

Download pushbullet.py-0.10.0.tar.gz from link listed  **above**

> **Note:**

> - You have to install pushbullet inside Mycroft virtual environment, for that do the following, download pushbullet

     tar -xvzf pushbullet.py-0.10.0.tar.gz
     cd pushbullet.py-0.10.0
     sudo /home/pi/.virtualenvs/mycroft/local/bin/python setup install

- Create your account on  [pushbullet.com](https://www.pushbullet.com/) to get your [Access Token](https://www.pushbullet.com/#settings)
- Install pushbullet on your phone 
- Make some contacts





----------


Installation
-------------------
**Clone PushbulletSkill repository** on third party skill directory

    cd  /opt/mycroft/third_party/

    git clone  https://github.com/jcasoft/PushbulletSkill.git

<i class="icon-cog"></i>Add 'PushbulletSkill' section in your Mycroft configuration file on: 

/home/pi/.mycroft/mycroft.ini

    [PushbulletSkill]
    api_key = "o.XXXXXXXXXX"  # <-- Replace with your Access token
    
    photo = "/opt/mycroft/third_party/mycroft-pushbullet-skill/script/photo.py"
    
    photo_img = "/tmp/photo.png"

> **Note:**

> - If use a different **third party skill directory** you have to change on [PushbulletSkill] section on /home/pi/.mycroft/mycroft.ini 
> and line 39 on 
> `/opt/mycroft/third_party/mycroft-pushbullet-skill/script/photo.py`

Restart Skills

    ./start.sh skills


----------


Features
--------------------

Currently this skill can do the following things (with some variation):

- **push** *juancarlos* barcelona is the best soccer team of the world **stop**
  

 > **Note:**
> - **push** is a PushMessageKeyword
> - ***juancarlos***  is the name of a contact that must exist in your pushbullet account, you can to pronounce the name or a part of the name from the beginning, if there is no contact, mycroft say a message that the contact not exist.
> -  **barcelona is the best soccer team of the world** is the message
> - **stop** to finish the message

- **photo**
 > **Note:**
> - **photo** is a PushMessageKeyword
> - The photo is sent to your pushbullet account



**Enjoy !**
--------

