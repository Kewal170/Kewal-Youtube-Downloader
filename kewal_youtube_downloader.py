import os
import sys

from pytube import Playlist
from pytube import YouTube

path_video_file = 'Videos_from_youtube'                                        # Make sure you have change your location
path_playlist_file = 'Playlist_from_youtube'


def video_info(link):                                  # This function will show information about that particular video
    print("-" * 50)
    print("Title : ", link.title)
    print("Total Views : ", link.views, "k")
    print("Channel url : ", link.channel_url)
    print("Published date : ", link.publish_date)
    print("-" * 50)


def playlist_info(link):   # This function will show total number of videos present in the playlist along with the title
    try:
        print("-" * 50)
        count = 1
        for video in link.videos:
            print(f"{count} : {video.title}")
            count += 1
        print("-" * 50)
    except Exception as e:
        print(f"Error - {e}")


def download_video(link):                                                   # This function will Download a single video
    try:
        print("-" * 50)
        print(f"Downloading :>  {link.title}")
        link.streams.get_highest_resolution().download(path_video_file)
        print("-" * 50)
        print("Download complete!")
        print(f"Output video location : /{path_video_file}/")
    except Exception as e:
        print(f"Error - {e}")


def download_playlist(link):   # This function will Download the whole playlist and store it in a channel's named folder
    os.mkdir(f"{path_playlist_file}/{link.owner}")
    try:
        print("-" * 50)
        for video in link.videos:
            print(f"Downloading :> {video.title}")
            video.streams.get_highest_resolution().download(f"{path_playlist_file}/{link.owner}")
        print("-" * 50)
        print("Download Complete!")
        print(f"Output video location : /{path_playlist_file}/{link.owner}/")
    except Exception as e:
        print(f"Error - {e}")


def help_menu():                                                                                             # Help menu
    print("-" * 50)
    print('''
        Syntax:-
        python kewal_youtube_downloader.py [command] [youtube video link]

        Commands:-
        info -> For retrieving video information
        playlist -> For retrieving playlist information
        d-video -> For downloading single video 
        p-video -> For downloading whole playlist

        NOTE: Make sure you have paste the link between Quotation Marks -- "link" / 'link'
        ''')
    print("-" * 50)


if len(sys.argv) == 3:                                                                                    # Main program
    command = sys.argv[1]
    youtube_link = sys.argv[2]
    if command == 'info' and youtube_link != "":
        youtube_link = YouTube(sys.argv[2])
        video_info(youtube_link)
    elif command == 'playlist' and youtube_link != "":
        youtube_link = Playlist(sys.argv[2])
        playlist_info(youtube_link)
    elif command == "d-video" and youtube_link != "":
        youtube_link = YouTube(sys.argv[2])
        download_video(youtube_link)
    elif command == 'p-video' and youtube_link != "":
        youtube_link = Playlist(sys.argv[2])
        download_playlist(youtube_link)
    else:
        print("Error Occurred!")
else:
    help_menu()
