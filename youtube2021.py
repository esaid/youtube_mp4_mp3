import youtube_dl
import time
import datetime
import os
import subprocess
liste_charactere = ['/', ':', '\\', '*', '?', '<', '>', '|', '.', '-', '"', "'", " "]  # caracteres a supprimer


def delete_character(s):
    for i in liste_charactere:
        s = s.replace(i, '')

    return s


# generation d'un string avec date et temps
date = str(datetime.datetime.now())
date = delete_character(date)
_filename = 'file' + date

mp4 = "%s.mp4" % _filename
mp3 = "%s.mp3" % _filename
url = input("URL: ")
#url = 'https://youtu.be/5JNaKBOWBnI'
#url = 'https://youtu.be/C0DPdy98e4c'
# exemple
# filename_rename : prend les 100 premiers caracteres et remplace les espaces par _

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(url, download=False)

    print('format      : %s' %(meta['format']))
    print('duration    : %s' %(meta['duration']))
    print('title       : %s' %(meta['title']))
    print('description : %s' %(meta['description']))

title = meta['title']

_filename_rename = title.replace(' ', "_")
_filename_rename = _filename_rename[:100]
_filename_rename = delete_character(_filename_rename)
print(_filename_rename)

print("\nDownloading....\n")
# si on ne veut que l'audio
# 'format': 'bestaudio/best',

_filename += '.mp4'
ydl_opts = {
    'format': 'mp4',
    'outtmpl': _filename,
    'noplaylist' : True,

}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])



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


