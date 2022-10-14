import os
from time import sleep
from subprocess import PIPE, run
import subprocess as sp
import json


# settings
sync_time = 2  # in hours
account = "[your_youtube_account_id]"
path = "[where_to_move_musics]"
archive_path = "[complete_path_to_archive_file]"
mformat = "mp3"
sleep_time = 0


# tool functions
def sync_time(hours):
    # can be used as a timer but not recommanded
    sleep(hours * 3600)


def out(command):
    print(os.system(command))


def account_video_list():
    # get the list of all videos on youtube
    request = 'youtube-dl --get-id --ignore-errors --no-warnings --playlist-reverse https://www.youtube.com/channel/' + \
        account + \
        '/playlists'
    ff = sp.getoutput(request)
    youtube_video_ids = ff.splitlines()
    # remove the last element of the list, which is empty
    return youtube_video_ids


def archive_remove(video_id):
    # remove each line containing the video_id in the archive.txt file
    with open(archive_path, "r") as f:
        lines = f.readlines()
    with open(archive_path, "w") as f:
        for line in lines:
            if video_id not in line:
                f.write(line)


def remove(video_id):
    # get the name of the video with youtube-dl on a variable
    request = 'youtube-dl --get-title --ignore-errors --no-warnings https://www.youtube.com/watch?v=' + video_id
    output = sp.getoutput(request)
    video_name = output.splitlines()[0]
    file_name = video_name + "." + mformat

    # for each folder in the musics folder
    for folder in os.listdir(path):
        # delete the file if it is in the folder
        if file_name in os.listdir(path+folder):
            os.system("rm '" + path+folder+"/"+file_name+"'")


# main functions
def down_sync():
    # download the playlist with youtube-dl, but only if the video is not in the archive.txt file
    request = 'youtube-dl -f bestaudio --add-metadata --rm-cache-dir --extract-audio --ignore-errors --no-warnings --playlist-reverse'
    request += ' --audio-format ' + mformat
    request += ' --download-archive '+archive_path
    request += ' https://www.youtube.com/channel/' + account + '/playlists'
    request += ' --output "' + path + '%(playlist)s/%(title)s.%(ext)s"'
    out(request)


def up_sync():
    account_video_ids = account_video_list()

    # get the list of all videos ids in the archive.txt file
    with open(archive_path, "r") as f:
        archive_video_ids = f.read().splitlines()

    #  for each video in the archive.txt file, check if it is still on youtube
    # if not, delete it
    for video_id in archive_video_ids:
        video_idee = video_id[8:]
        if video_idee not in account_video_ids:
            remove(video_idee)
            archive_remove(video_idee)


# main sync loop
down_sync()
sync_time(1)
up_sync()
