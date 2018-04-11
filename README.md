**PushbulletSkill**
===================

An skill to use with Mycroft that allows you to send messages, 10 seconds audio file and photos using **Pushbullet**





Prerequisites for Pushbullet
-------------
- Create your account on  [pushbullet.com](https://www.pushbullet.com/) to get your [API](https://www.pushbullet.com/signin?next=%2F) 
- Install pushbullet on your phone 
- Make some contacts

**Conect your USB Camera to Mycroft installation (Mark1, Desktop, Picroft)**

----------



Install Methon on Mark1 and other devices
-------------------
    install push bullet



Install Using MSM (Mycroft Skill Manager)
-------------------

    msm install https://github.com/jcasoft/PushbulletSkill.git



Manual Method not for Mark1
-------------------
**Clone PushbulletSkill repository** on third party skill directory

    cd  /opt/mycroft/skills
    git clone  https://github.com/jcasoft/PushbulletSkill.git
    cd PushbulletSkill
    workon mycroft (Only if you have installed Mycroft on Virtualenv)
    sudo apt-get install lame libopencv-dev python-opencv
    sudo pip install -r requirements.txt



Authorization:
-------------------
Visit the  [Skill settings for Pushbullet ](https://home.mycroft.ai/#/skill) and enter the API get on **Prerequisites for Pushbullet**




Restart Skills



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

