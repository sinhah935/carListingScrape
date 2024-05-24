from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver
chrome_options = Options()
# chrome_options.add_argument("--headless")  # This doesn't work for carvana because they have some Ddos protection by cloudflare. 
# It wont allow you to scrap their site programatically 
service = Service('/usr/local/bin/chromedriver')  # Update with the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website
url = "https://www.carvana.com/cars/filters?utm_source=google&utm_medium=sem_nb&utm_campaign=15848039259&utm_content=133778262124&utm_target=kwd-26668790&utm_creative=656002080421&utm_device=c&utm_adposition=&gad_source=1&gclid=EAIaIQobChMI3JKf5KibhgMVcUtHAR0tnw29EAAYASAAEgL4ffD_BwE&cvnaid=eyJmaWx0ZXJzIjp7Im1ha2VzIjpbeyJuYW1lIjoiQk1XIiwicGFyZW50TW9kZWxzIjpbeyJuYW1lIjoiTTMifV19XX19?lang=en"
driver.get(url)

# Scroll down to load more listings
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get page source and close the driver
page_source = driver.page_source
driver.quit()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find all divs with class 'group/main m:border m:border-grey-2 m:border-solid m:h-[397px] m:min-h-[365px] m:rounded-[6px]'
result_tiles = soup.find_all('div', class_='group/main m:border m:border-grey-2 m:border-solid m:h-[397px] m:min-h-[365px] m:rounded-[6px]')
# print(result_tiles)
# Iterate over each result tile
for result_tile in result_tiles:
    # Find car model
    car_model = result_tile.find('p', class_='font-bold leading-[24px] text-[18px] truncate').text.strip()
    # Find price
    price = result_tile.find('div', class_='-mb-[2px] flex font-bold gap-8 items-center text-2xl text-blue-6').text.strip()
    # Find monthly payment
    monthly_payment = result_tile.find('div', class_='flex gap-4').text.strip()
    
    # Print the extracted information
    print("Car Model:", car_model)
    print("Price:", price)
    print("Monthly Payment:", monthly_payment)
    print()
