# Functionnal YouTube music sync
This programm is a simple bot who get videos/musics saved in a given account. This robot have the ability to retrieve the videos in playlists and keep them in order. 

# Description
This is a Python script that syncs a YouTube channel with a local folder of music files.

The script has three main functions:

down_sync: downloads the playlist from the specified YouTube channel and adds the video information to an archive file
up_sync: checks the archive file for videos that have been deleted from the channel and removes those files from the local folder
remove: removes a single video file from the local folder

The script has several settings that can be configured, including the YouTube channel ID, the local folder paths, and the format of the music files.

# upsync / downsync functions
The two steps of synchronisation  are separated in two funtion.
The downsync give the ability for the program to download musics who are on youtube but not in the archive.txt folder.
Then, the upsync function was created in order to update the archive.txt file and delete musics who are on YouTube but not on the server.


