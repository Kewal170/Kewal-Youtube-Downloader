import os
import sys
from datetime import datetime
import yt_dlp as youtube_dl
import speedtest

# Define paths for saving downloaded videos and playlists
path_video_file = 'Videos_from_youtube'
path_playlist_file = 'Playlist_from_youtube'

# Ensure output directories exist
def make_output_files():
    os.makedirs(path_video_file, exist_ok=True)
    os.makedirs(path_playlist_file, exist_ok=True)

# Check internet speed
def speed_testing():
    try:
        st = speedtest.Speedtest()
        download_result = st.download()
        print(f"Download speed: {download_result / 1024 / 1024:.2f} Mb/s")
    except Exception as e:
        print(f"Speed test error: {e}")

# Print video information
def video_info(url):
    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
        'no_warnings': True,
        'dumpjson': True
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print("-" * 50)
            print(f"Title: {info.get('title')}")
            print(f"Total Views: {info.get('view_count')}")
            print(f"Channel URL: {info.get('uploader_url')}")
            print(f"Published Date: {info.get('upload_date')}")
            print("-" * 50)
    except Exception as e:
        print(f"Error - {e}")

# Print playlist information
def playlist_info(url):
    ydl_opts = {
        'quiet': True,
        'noplaylist': False,
        'no_warnings': True,
        'dumpjson': True
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print("-" * 50)
            for count, video in enumerate(info.get('entries', []), start=1):
                print(f"{count}: {video.get('title')}")
            print("-" * 50)
    except Exception as e:
        print(f"Error - {e}")

# Download a single video
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(path_video_file, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True
    }
    try:
        print(f"\n> Downloading video: {url}")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download complete! Location: {path_video_file}")
    except Exception as e:
        print(f"Error - {e}")

# Download an entire playlist
def download_playlist(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(path_playlist_file, '%(uploader)s/%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True
    }
    try:
        print(f"\n> Downloading playlist: {url}")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download complete! Location: {path_playlist_file}")
    except Exception as e:
        print(f"Error - {e}")

# Display help menu
def help_menu():
    print("-" * 50)
    print('''
        Syntax: python youtube_downloader.py [command] [youtube video link]

        Commands:
        info -> For retrieving video information
        playlist -> For retrieving playlist information
        v-download -> For downloading single video
        p-download -> For downloading whole playlist

        Note: Ensure the link is enclosed in quotation marks: "link" or 'link'
        ''')
    print("-" * 50)

# Ensure directories are created
make_output_files()

# Main program logic
if len(sys.argv) == 3:
    command = sys.argv[1]
    youtube_link = sys.argv[2]
    try:
        if command == 'info':
            video_info(youtube_link)
        elif command == 'playlist':
            playlist_info(youtube_link)
        elif command == "v-download":
            download_video(youtube_link)
        elif command == 'p-download':
            download_playlist(youtube_link)
        else:
            print("Invalid command!")
    except Exception as e:
        print(f"Error - {e}")
else:
    help_menu()
