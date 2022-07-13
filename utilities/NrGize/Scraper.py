from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Scraper: 

    def __init__(self, zip, url="https://www.nrgizejuice.com/locator/"):
        self.zip = zip
        self.url = url

    def chrome(headless=True):
    # support to get response status and headers
        opt = webdriver.ChromeOptions()
        if headless:
            opt.add_argument("--headless")
        opt.add_argument("--disable-xss-auditor")
        opt.add_argument("--disable-web-security")
        opt.add_argument("--allow-running-insecure-content")
        opt.add_argument("--no-sandbox")
        opt.add_argument("--disable-setuid-sandbox")
        opt.add_argument("--disable-webgl")
        opt.add_argument("--disable-popup-blocking")
        # opt.add_experimental_option("detach", True)
        browser = webdriver.Chrome("../chromedriver/chromedriver", options=opt)
        return browser

    def getBrowser(self):
        driver = self.chrome()
        return driver

    def process(self):
        driver = self.getBrowser()
        driver.get(self.url)
        deny_cookie_box = driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline")
        deny_cookie_box.click()
        zip = self.zip
        search_box = driver.find_element(By.ID, "qInnerID")
        driver.implicitly_wait(100)
        search_box.send_keys(zip)
        # click search
        go_search = driver.find_element(By.ID, "submit-btn")
        go_search.click()
        print("counting")
        facility_components = driver.find_elements(By.CLASS_NAME, "listing")
        for facility in facility_components:
            id_ = facility.get_attribute("id")
            self.write_facility_component("Store Number: " + id_ + "\n" + facility.text)

        
    def write_facility_component(self, message):
        dir_name = './html_files/'
        file_name = datetime.today().strftime('%Y-%m-%d').replace("-","_") + "_" + str(self.zip) + ".txt"
        with open(dir_name + file_name, "a") as f:
            f.write(message + "\n\n")