#Installation And How To Use lyricGrabberSearch.py
This lyric scraper uses Chrome and AdBlock to find and scrape lyrics to a given song on genius.com
I added an adblocker to make the browser load quicker.

##Installation
- Install the latest version of Python
- Install argparse: 'pip install argparse'
- Install Selenium: 'pip install selenium'
- Install webdriver-manager: 'pip install webdriver-manager'
- Install AdBlock on Chrome: https://chromewebstore.google.com/detail/adblock-%E2%80%94-block-ads-acros/gighmmpiobklfepjocnamgkkbiglidom?hl=en-US
- Line 12: Change 'InsertSystemName' to your system name. This will allow the program to utilize the AdBlock.

##How To Use
Program will first ask for a song title. Type the title into terminal.
Program will then ask for the artist. Type the artist into terminal.
A new Chrome browser will open and automate to the genius.com website. An AdBlock browser will also open, which confirms its use. (You can close the AdBlock tab if you'd like)
The program will load genius.com, insert the song title and artist into the search bar, proceed with the search, pick the first result, and print the lyrics.
