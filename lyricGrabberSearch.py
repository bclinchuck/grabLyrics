from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import argparse
from selenium.webdriver.chrome.options import Options

cOptions = Options()
cOptions.add_argument('--ignore-certificate-errors')
cOptions.add_argument('--disable-ssl-cert-validation')


# Set up argument with user inputs
song = input("Enter the song title: ")
artist = input("Enter the artist: ")
parser = argparse.ArgumentParser()
parser.add_argument("song", type=str, nargs="?", default=song)  
parser.add_argument("artist", type=str, nargs="?", default=artist)  
args = parser.parse_args()
print(f"Searching for {args.song} by {args.artist}")

# Open genius.com
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=cOptions)
driver.get("https://genius.com/")
wait = WebDriverWait(driver, 10)

# Locate the search bar and search with paramters
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
query = f"{args.song} {args.artist}"
search_box.send_keys(query)
search_box.submit()

# Wait for search results and click the first result
first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mini_card-info")))
first_result.click()

# Locate the lyrics and set allLyrics to the text
pause = WebDriverWait(driver,5)
lyrics = pause.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div[data-lyrics-container='true']")))
songTitle = pause.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))).text
artistName = pause.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[href*='/artists/']"))).text

# Print and close browser
print("\nLyrics to " + songTitle + " by " + artistName + ":\n")
allLyrics = "\n".join([element.text for element in lyrics])
print(allLyrics)
driver.quit()