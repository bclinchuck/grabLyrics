from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options() # Will keep browser open after search is complete
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

song = input("Enter the song title: ")
artist = input("Enter the artist: ")
print("Searching for " + song + " by " + artist)

searchArt = ""
searchSong = ""
for char in artist:
    if char == " ":
        searchArt = searchArt + "-"
    else:
        searchArt = searchArt + char
for char in song:
    if char == " ":
        searchSong = searchSong + "-"
    else:
        searchSong = searchSong + char

driver.get("https://www.genius.com/" + searchArt + "-" + searchSong + "-lyrics")
print(driver.dialog)