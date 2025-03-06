# Installation And How To Use lyricGrabberSearch.py
This lyric scraper uses Chrome to find and scrape lyrics to a given song on genius.com

## Installation
- Download both `requirements.txt` and `lyricGrabberSearch.py`
- Install the latest version of Python
- Install the used Python libraries in your terminal with: `pip install -r requirements.txt`
> [!NOTE]
> - If system cannot find files through downloads, drag the downloads to desktop and type  `cd Desktop` in terminal, click enter, and try `pip install -r requirements.txt` again.

## How To Use
- Open terminal and install `requirements.txt` as stated above.
- Run script by typing `python lyricGrabberSearch.py` for Windows OS and `python3 lyricGrabberSearch.py` for Mac OS.
- Program will first ask for a song title. Type the title into terminal. Press enter.
  > Enter the song title:
  >
  > **Ex)** Enter the song title: Sidelines
- Program will then ask for the artist. Type the artist into terminal. Press enter.
  > Enter the artist:
  >
  > **Ex)** Enter the artist: Wallows
- A new Chrome browser will open and automate to the genius.com website.

The program will load genius.com, insert the song title and artist into the search bar, proceed with the search, pick the first result, and print the lyrics.
