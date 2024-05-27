import requests
import time
from bs4 import BeautifulSoup
import csv
#to get past javaScript
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

#carvana
#url = 'https://www.carvana.com/cars/filters?utm_source=google&utm_medium=sem_nb&utm_campaign=15848039259&utm_content=133778262124&utm_target=kwd-26668790&utm_creative=656002080421&utm_device=c&utm_adposition=&gad_source=1&gclid=EAIaIQobChMI3JKf5KibhgMVcUtHAR0tnw29EAAYASAAEgL4ffD_BwE&cvnaid=eyJmaWx0ZXJzIjp7Im1ha2VzIjpbeyJuYW1lIjoiQk1XIiwicGFyZW50TW9kZWxzIjpbeyJuYW1lIjoiTTMifV19XX19'

# Navigate to the website
#url = "https://www.carvana.com/cars/filters?utm_source=google&utm_medium=sem_nb&utm_campaign=15848039259&utm_content=133778262124&utm_target=kwd-26668790&utm_creative=656002080421&utm_device=c&utm_adposition=&gad_source=1&gclid=EAIaIQobChMI3JKf5KibhgMVcUtHAR0tnw29EAAYASAAEgL4ffD_BwE&cvnaid=eyJmaWx0ZXJzIjp7Im1ha2VzIjpbeyJuYW1lIjoiQk1XIiwicGFyZW50TW9kZWxzIjpbeyJuYW1lIjoiTTMifV19XX19?lang=en"

#cargurus
#url = "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=11219&inventorySearchWidgetType=AUTO&sortDir=ASC&sourceContext=cargurus&distance=50&sortType=BEST_MATCH&entitySelectingHelper.selectedEntity=d390"

#cars.com
#url = "https://www.cars.com/shopping/brooklyn-ny/"


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def source(url):
    
    # Set up Selenium WebDriver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # This doesn't work for carvana because they have some Ddos protection by cloudflare. 
    # It wont allow you to scrap their site programatically 
    service = Service()  # Update with the path to your chromedriver, finds path of chromedriver w/o parameter
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    # Scroll down to load more listings
    SCROLL_PAUSE_TIME = 3
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

    return page_source

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def parsedCars(page_source, tag, clAss):
    soup = BeautifulSoup(page_source, "html.parser")
    #print(soup)

    listCars = soup.find_all(tag, class_= clAss)
    
    return listCars

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#csv conversion
# file_name = 'm3listingmk1.csv'

# with open(file_name, 'w', newline = '') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(
#         ['Car',
#          'Miles',
#          'Price']
#     )

#     for car in m3Cars:
#         theCar = car.find('p', class_ = 'font-bold leading-[24px] text-[18px] truncate').text.strip()
#         miles = car.find('span', class_ = 'shrink-0').text.strip()
#         price = car.find('div', class_ = '-mb-[2px] flex font-bold gap-8 items-center text-2xl text-blue-6').text.strip()

#         csvwriter.writerow([theCar, miles, price])

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def csvConvert(csvName, listOfCars, infoType, carInfo):
    file_name = str(csvName) + '.csv'

    with open(file_name, 'w', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(infoType)

        for car in listOfCars:
            currInfo = []
            for tag, cass in carInfo:
                info = car.find(tag, class_ = cass).text.strip()
                currInfo.append(info)
            csvwriter.writerow(currInfo)

    return csvwriter

def csvConvertwMake(csvName, listOfCars, infoType, carInfo, make: str):
    file_name = str(csvName) + '.csv'

    with open(file_name, 'w', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(infoType)

        for car in listOfCars:
            currInfo = []
            for tag, cass in carInfo:
                info = car.find(tag, class_ = cass).text.strip()
                currInfo.append(info)

            if currInfo[0].find(make) != -1:
                csvwriter.writerow(currInfo)

    return csvwriter


    
url = "https://www.cars.com/shopping/brooklyn-ny/#vehicle-card-0fcabc1e-e747-4ecd-8192-e9aba6dc38f5"
TYPE = 'div'
CLASS = 'vehicle-card vehicle-card-with-reviews ep-theme-hubcap'
CSVNAME = 'carListings'
LISTOFINFO = ['Car', 'Miles', 'Price', 'Owner Report']
MAKE = "Ford"
carInfo = [('h2', 'title'), ('div', 'mileage'), ('span', 'primary-price')]
        
source = source(url)

listOfCars = parsedCars(source, TYPE, CLASS)

csvConvertwMake(CSVNAME, listOfCars, LISTOFINFO, carInfo, MAKE)







    
