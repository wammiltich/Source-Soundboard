# Source-Soundboard
Exists in 2 parts; one script to download audio (optional) and another to write these files to the CSGO folder.
Source has a command (voice_inputfromfile 0/1) that allows you to play an audio file from your machine as a 'mic'.
However there are some conditions for this file.
It MUST be saved in an exact location + name within the game folder ( C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\voice_input.wav ), and the .wav file must be 16 bit, mono channel, and have a rate of 22050Hz

Any other location and any other filename (even if saved in the same folder) will not work. Any other settings for the .wav will make it inaudible in-game.
AFAIK there is no way around this unfortunately.

Therefore, soundboard.py works as an intermediator that watches for key presses, and if a key that is mapped is pressed, it will write the corresponding file to that location.
There is a series of commands all strung together that you need to paste into cs terminal to enable this trick.
So, the overall process to get this thing to work on a new machine is as follows:

1) 
Download both .py's, and scroll through them - try to make sense of my spaghetti comments.
Fix any hard coded paths that still exist in the code to match your PC

2)
Try the youtube to mp3 script - you'll get an error from the pytube module. Btw go install that with pip -- left a comment below on how to use it if you're unfamiliar. Youtube changed something and the module has not been updated to reflect that change yet. There's an explanation on stackoverflow on value to change and how to do it - takes like 20 seconds. I'll link it here once I find it, but if you look up the error it throws you should be able to get to it real quick.
Once you confirm you're able to run it and save an .mp3 you're good to go on.

3)
Now you need to prep that audio file so that csgo/source can understand it correctly. I use audacity for this, free and 'ez'. Splice and trim the audio to get the segment you want to use. At some point you'll need FFMPEG for audacity to work - might come with it I don't even know for sure, but also just a quick install if not. Again there's a discussion on steamcommunity somewhere on how to prep these files with audacity that I followed; I'll link it here when I find it. But, essentially all you need to do is split it to 2 channels and delete the bottom one to make it "mono", change it to 16 bit and set the project rate (bottom left) to 22050Hz. Save it as a .wav when you're done.

4)
Now this is the easy part, hoo-rah. Open up soundboard.py and take a gander at the 'soundset'(s). To make a 'set' as I call them, provide a path to the folder containing your processed .wav files. Just now realizing I should've written a class for this, but, whatever. I'll modify that later --- anyway. Paste your path to the audio folder (audio_dir = r"{path goes here}"). Now you need to map those sounds to keys. If you have an audio file, suppose it's "TestSound.wav", just list it as "TestSound" in the mapping - regex takes care of the rest. In the mappings (dictionary), the key is the...shocker here... KEY of the dictionary, and the audio file name is the value. You can map to any key as your heart desires. I used the keyboard module, they have a list of the names/string values for each key on their documentation - but most of it is straightforward.

5)
I don't use IDE's, I use notepad ++ for everything. So, if you're having any trouble figuring out how to run these files, open up CMD and paste "python C:\Users\blablabla\----\soundboard.py" and it'll instantiate. Don't have the full path? Shift+RClick on the file and there'll be a new option: "Copy as path". Hit that, and paste it. Voila. If you get any errors regarding "No package/module named {something}", use pip. If you don't know what pip is - it's your new bestfriend. Need the keyboard module? Open up CMD and run "pip install keyboard". Crazy stuff! But be careful - pip is run off of PyPi and anyone can upload things to it if the name hasn't already been taken. Always check out the project details on the website before installing it - there is little to no moderation! People WILL upload malicious packages and malware that are a slight typo away from a popular package. Be safe and measure twice!

6) 
If you got it all set up right, you should be seeing the terminal window print out the path to the audio file when you press the corresponding key. If you see that, the voice_input.wav file is successfully updating to each sound. Now that it's working, open up CSGO and paste this ugly command in the dev terminal: bind mouse3 music_on;alias music_on "voice_inputfromfile 1;+voicerecord; voice_loopback 1; bind mouse3 music_off";alias music_off "voice_inputfromfile 0;-voicerecord; voice_loopback 0; bind mouse3 music_on". Pretty gross - but makes it where you can hear the voicelines/sounds as well. Press middle mouse to start, press it again to stop. GLHF
