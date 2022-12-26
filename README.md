# youtube-music
A simple youtube-dl download bot made in python.
The script downloads the audio of video from youtube.
Once downloaded, FFMpeg convert the audio from mp4a to mp3.

# upsync / downsync functions
The two steps of synchronisation  are separated in two funtion.

Upsync get the list of videos/musics in the playlist. Then, for each file it check with the archive.txt if it's on the server. 

Downsync download the videos that arent in the archive.
All the program is working in my raspverry. 
