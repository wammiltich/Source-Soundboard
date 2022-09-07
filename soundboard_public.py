'''
Hey MTV, welcome to my crib
Follow the comments to figure out how to set up a "soundset"/preset of soundboard
Essentially; make a folder of .wav files that meet the csgo/source engine requirements and turn it into a dictionary
(pssst i hate paid software so just use audacity to modify mp3 files to these requirements):
- 16 bit 
- mono channel
- 22050 Hz "project rate"   

Then, for each preset provide the path to the folder as audio_dir
and then map the keys as seen below. Have fun!

paste <this> into CSGO terminal to add functionality to middle mosue button (click to start, click to stop): 

bind mouse3 music_on;alias music_on "voice_inputfromfile 1;+voicerecord; voice_loopback 1; bind mouse3 music_off";alias music_off "voice_inputfromfile 0;-voicerecord; voice_loopback 0; bind mouse3 music_on"
'''

import os,keyboard,time,shutil,re
from keyboard import *


# Should be fine, but updaate if your path is different
dest = r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\voice_input.wav"
library = {} 

# Allows you to have serveral 'sets', select the one you want to use by changing this value
# \/\/\/\/\/\/
soundset = 1
# ^^^^^^^^^
" -------------- "
def assignSound(audiopath):
    global dest,currentsound
    if currentsound != audiopath:
        currentsound = audiopath
        shutil.copy(audiopath,dest)
        print(f"SET SOUND TO {audiopath}",flush=True)
'''
set 1
'''
if soundset ==1:
    # this is the path to the folder where the FINAL( meets requirements) processed .wav files are for the preset: 
    audio_dir = r"C:\Users\---\b1battledroid_voicelines\processed" # censored for privacy
    for file in os.listdir(audio_dir):
        fname = re.compile(r"(.*)\.wav").findall(file)[0] # *
        library[fname] = os.path.join(audio_dir,file)
    # the names in the brakcets (e.g. 'cry') are the filenames minus extension, such as "cry.wav"
    # the regex hanldes the rest :)  *
    soundKeys = {"NUM_1":library["cry"],
                 "NUM_2":library["pewpewpew"],
                 "NUM_3":library["legoDeath"],
                 "NUM_4":library["rogerroger"],
                 "NUM_5":library["independentthinkers"],
                 "NUM_6":library["targetaquired"],
                 "NUM_7":library["sing"],
                 "NUM_8":library["rush"],
                 "NUM_9":library["woohoo"]}
'''
set 2
'''
elif soundset ==2:
    audio_dir = r"C:\Users\---\songs\processed"
    for file in os.listdir(audio_dir):
        fname = re.compile(r"(.*)\.wav").findall(file)[0]
        library[fname] = os.path.join(audio_dir,file)
    soundKeys = {#"NUM_1":library[""],
                 # #"NUM_2":library[""],
                 # #"NUM_3":library[""],
                 # #"NUM_4":library[""],
                 "NUM_5":library["VineBoom"],
                 "NUM_6":library["Danger"],
                 "NUM_7":library["Toto"],
                 "NUM_8":library["BonieTyler"],
                 "NUM_9":library["DangerZone"]}
# NOTE: comment out keys you dont use like I've done for set 2 or it will raise an error

keys = soundKeys.keys()
currentsound = ""
while True:
    for key in keys:
        if is_pressed(key):assignSound(soundKeys[key])
    time.sleep(.01) # buffer to make sure you don't kill ur CPU while watching keys
