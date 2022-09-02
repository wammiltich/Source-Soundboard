from pytube import YouTube
'''
I recall there being an issue with this module; youtube changed something to make it not work
when you get that error just look it up - there was a thread on stackoverflow on what values to change in 
the module file to adjust for youtube's change
'''
import os
  
# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or r'C:\---\defaultdirectory'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")