import requests
import time
from bs4 import BeautifulSoup
import csv
#to get past javaScript
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.carvana.com/cars/filters?utm_source=google&utm_medium=sem_nb&utm_campaign=15848039259&utm_content=133778262124&utm_target=kwd-26668790&utm_creative=656002080421&utm_device=c&utm_adposition=&gad_source=1&gclid=EAIaIQobChMI3JKf5KibhgMVcUtHAR0tnw29EAAYASAAEgL4ffD_BwE&cvnaid=eyJmaWx0ZXJzIjp7Im1ha2VzIjpbeyJuYW1lIjoiQk1XIiwicGFyZW50TW9kZWxzIjpbeyJuYW1lIjoiTTMifV19XX19'


# driver = webdriver.Chrome()#unspecified path should look for path to chrome webdriver

# driver.get(url)
# time.sleep(5)

# page_source = driver.page_source #get page source

#parser
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
time.sleep(5)
print(soup.prettify())


m3Cars = soup.find_all('p', class_ = 'font-bold leading-[24px] text-[18px] truncate')

print(m3Cars)


# miles = soup.find_all('p', class_ = 'HczmlC')

#csv conversion
# file_name = 'm3listingmk1.csv'

# with open(file_name, 'w', newline = '') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(
#         ['Car',
#          'Miles']
#     )

#     for car, miles in zip(m3Cars, miles):
#         theCar = car.text
#         m = miles.text

#         csvwriter.writerow(
#             [theCar,
#              m]
#         )


    
