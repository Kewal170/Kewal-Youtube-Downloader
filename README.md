# YouTube Downloader with Speed Test

## Overview

This Python project provides a command-line interface for downloading YouTube videos and playlists. It also includes a function to test the internet speed before downloading. The tool uses `yt-dlp` (a fork of `youtube-dl`) for downloading videos and `speedtest` for checking internet speed.

## Features

- **Download Single Video**: Download a specific YouTube video.
- **Download Playlist**: Download all videos from a YouTube playlist.
- **Video and Playlist Information**: Retrieve and display information about a single video or a playlist.
- **Speed Test**: Measure and display internet download speed before downloading.

## Requirements

- Python 3.6+
- `yt-dlp`
- `speedtest-cli`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Install dependencies:**

    Create a `requirements.txt` file with the following content:

    ```
    yt-dlp
    speedtest-cli
    ```

    Install the dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Commands

- **Retrieve Video Information**

    ```bash
    python youtube_downloader.py info "https://www.youtube.com/watch?v=VIDEO_ID"
    ```

- **Retrieve Playlist Information**

    ```bash
    python youtube_downloader.py playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID"
    ```

- **Download Single Video**

    ```bash
    python youtube_downloader.py v-download "https://www.youtube.com/watch?v=VIDEO_ID"
    ```

- **Download Playlist**

    ```bash
    python youtube_downloader.py p-download "https://www.youtube.com/playlist?list=PLAYLIST_ID"
    ```

### Example

To download a single video:

```bash
python youtube_downloader.py v-download "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
