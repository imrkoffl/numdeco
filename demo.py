'''
Demo using pytube and numdeo
'''

#importing libaries
from numdeco import deco, decoco, indeco, indecoco
from pytube import YouTube

ytLink = 'https://youtu.be/9hvjBi4PKWA'
video = YouTube(ytLink)

#video name and real time views
print(str(video.title)+'\n'+'Real time views : '+str(video.views))

#video views using deco
deco(video.views)
#video views using decoco
decoco(video.views)

#indian version

#video views using indeco
indeco(video.views)
#video views using indecoco
indecoco(video.views)
