from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def make_reservation(reservation_info):
    driver = webdriver.Chrome('C:/Users/sajja/Downloads/chromedriver-win64.exe')
    
    driver.get("https://libcal.dartmouth.edu/space/" + reservation_info["space_id"])

    # You may need to wait a few seconds for the page to load
    time.sleep(5)

    # Select date
