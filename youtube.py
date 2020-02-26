# -*- coding: utf-8 -*-
from pytube import YouTube
import os
import subprocess
import time
import datetime

liste_charactere = ['/', ':', '\\', '*', '?', '<', '>', '|', '.', '-','"',"'"," "]  # caracteres a supprimer
def delete_character (s):
    for i in liste_charactere:
       s = s.replace(i,'')

    return s


# generation d'un string avec date et temps
date = str(datetime.datetime.now())
date = delete_character(date)
_filename = 'file' + date

mp4 = "%s.mp4" % _filename
mp3 = "%s.mp3" % _filename
url = input("URL: ")
# url = "https://www.youtube.com/watch?v=ITnLNoWOwFU"  exemple
# filename_rename : prend les 100 premiers caracteres et remplace les espaces par _
_filename_rename = YouTube(url).title.replace(' ', "_")[:100]
_filename_rename = delete_character(_filename_rename)
print(_filename_rename)
# Download
print("\nDownloading....\n")
YouTube(url).streams.first().download(filename=_filename)
time.sleep(1)
print("\nConverting\n")
# Converting mp4 vers mp3
ffmpeg_param = 'ffmpeg -i %s -vn %s' % (mp4, mp3)
# print (ffmpeg_param)
ffmpeg = ffmpeg_param
subprocess.call(ffmpeg, shell=True)

time.sleep(1)
try:
    os.rename(mp4, _filename_rename + ".mp4")
except:
    print("je n'arrive pas a renommer le fichier mp4")
time.sleep(1)
try:
    os.rename(mp3, _filename_rename + ".mp3")
except:
    print("je n'arrive pas a renommer le fichier mp3")
time.sleep(1)
# end
print("\nEnd\n")
