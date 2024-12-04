""" YOUTUBE DOWNLOADER FOR THE LOW WIFI"""

from pytube import YouTube
from sys import argv


link = argv[1]
Youtube_object = YouTube(link)

print("Title: ",Youtube_object.title)
print("Views:", Youtube_object.views)

object2 = Youtube_object.streams.get_lowest_resolution()
object2.download('/Users')
