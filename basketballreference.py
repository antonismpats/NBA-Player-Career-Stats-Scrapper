from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initializing the driver and setting the window open for the whole time
options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://google.com")

#Wait until the page is loaded properly and Deny cookies based on the XPATH of the Deny Cookies button
WebDriverWait(driver, 5).until(
     EC.presence_of_element_located((By.XPATH, '//*[@id="W0wltc"]'))
 )
language = driver.find_element(By.XPATH, '//*[@id="W0wltc"]')
language.click()

#Enter and search hoops reference
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("hoops reference" + Keys.ENTER)

#Open the link to the site
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Basketball-Reference"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Basketball-Reference")
link.click()

#Deny cookies again
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='qc-cmp2-ui']/div[2]/div/button[2]"))
)

language = driver.find_element(By.XPATH, "//*[@id='qc-cmp2-ui']/div[2]/div/button[2]")
language.click()

#Find and click on the player 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='players']/div[1]/a[7]"))
)

nba_player = driver.find_element(By.XPATH, "//*[@id='players']/div[1]/a[7]")
nba_player.click()

time.sleep(2)

#Find his/her name
player_name_place = driver.find_element(By.TAG_NAME, 'h1')
player_name = player_name_place.text

print(f'You just selected: {player_name}, with the following career stats:')

#Find and print the stats
player_stats_place = driver.find_element(By.CLASS_NAME, 'p1')
player_stats = player_stats_place.text
print(player_stats)








