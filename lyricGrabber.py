from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#import undetected_chromedriver as uc
#driver = uc.Chrome()

chop = webdriver.ChromeOptions()
chop.add_extension('Adblock-Plus_v1.4.1.crx')
#driver = webdriver.Chrome()

#chrome_options = Options()
#chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          chrome_options=chop)

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
#print(driver.page_source)
##time.sleep(5)
pause = WebDriverWait(driver,30)
##lyrics = pause.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "Lyrics-sc-37019ee2-1 jRTEBZ")]')))
lyrics = pause.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div[data-lyrics-container='true']")))
allLyrics = "\n".join([element.text for element in lyrics])
print(allLyrics.text)
#print(driver.page_source)
#lyrics = driver.find_elements(By.CLASS_NAME, "Lyrics-sc-37019ee2-1 jRTEBZ")
#print(driver.find_element(By.XPATH, '//*[contains(@class, "Lyrics-sc-37019ee2-1 jRTEBZ")]').text)
driver.quit()