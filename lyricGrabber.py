from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

extPath = "/Users/InsertSystemName/Library/Application Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/6.15.0_1"
#Change "InsertSystemName" to your system name and get the Chrome extension AdBlock
#Add the extension here: https://chromewebstore.google.com/detail/adblock-%E2%80%94-block-ads-acros/gighmmpiobklfepjocnamgkkbiglidom?hl=en-US

options = Options()
options.add_argument(f"--load-extension={extPath}")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Get user input
song = input("Enter the song title: ")
artist = input("Enter the artist: ")
print("Searching for " + song + " by " + artist)

#Changes spaces to "-" for successful link
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

#Go to website with given artist and song
driver.get("https://www.genius.com/" + searchArt + "-" + searchSong + "-lyrics")

#Let website load for 30 seconds
pause = WebDriverWait(driver,5)
#Locate the lyrics and set allLyrics to the text
lyrics = pause.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div[data-lyrics-container='true']")))
allLyrics = "\n".join([element.text for element in lyrics])
#Print and close browser
print(allLyrics)
driver.quit()
