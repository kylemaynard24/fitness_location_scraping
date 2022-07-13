from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException 

class Scraper: 
    def __init__(self, state):
        self.state = state
        # https://www.lafitness.com/Pages/findclubresultszip.aspx?state=FL
        self.url = 'https://www.lafitness.com/Pages/findclubresultszip.aspx?state=' + state

    def chrome(headless=False):
    # support to get response status and headers
        opt = webdriver.ChromeOptions()
        # if headless:
        #     opt.add_argument("--headless")
        opt.add_argument("--disable-xss-auditor")
        opt.add_argument("--disable-web-security")
        opt.add_argument("--allow-running-insecure-content")
        opt.add_argument("--no-sandbox")
        opt.add_argument("--disable-setuid-sandbox")
        opt.add_argument("--disable-webgl")
        opt.add_argument("--disable-popup-blocking")
        browser = webdriver.Chrome("../chromedriver/chromedriver", options=opt)
        # browser.implicitly_wait(10)
        # browser.set_page_load_timeout(20)
        return browser

    def getBrowser(self):
        driver = self.chrome()
        return driver

    def check_next_button(self, driver, id='ctl00_MainContent_lnkNextTop'):
        found = False
        next_button = None
        print(driver)
        driver.implicitly_wait(10)
        try:
            next_button = driver.find_element_by_id(id)
            # driver.find_element_by_xpath(By.ID, id)
        except NoSuchElementException:
            print("next button not found")
        found = True
        print(next_button)
        print(found)
        return found

    def click_next_button(self, driver):
        next_button_found = False
        print('in test next button')
        a_s = driver.find_elements(By.TAG_NAME, "a")
        for i in range(0, len(a_s)):
            if a_s[i].text == 'Next':
                a_s[i].click()        
                print("found next button!")
                next_button_found = True
        if next_button_found == True:
            print("next_button_found True")
        return next_button_found    


    def process(self):
        driver = self.getBrowser()
        driver.get(self.url)
        try:
            select = Select(driver.find_element(By.ID, "ctl00_MainContent_ddlPageSize"))
            select.select_by_value("50")
            facility_components = driver.find_elements(By.CLASS_NAME, 'colclass-sm-7')
            next_button = True
            while next_button == True: 
                for facility in facility_components:
                    self.write_facility_component(facility.text)
                # print('There were ' + str(len(facility_components)) + " found")
                # print("BEFORE NEXT BUTTON = " + next_button)
                next_button = self.click_next_button(driver)
                # print("AFTER NEXT BUTTON = " + next_button)
        except:
            facility_components = driver.find_elements(By.CLASS_NAME, 'colclass-sm-7')
            for facility in facility_components:
                self.write_facility_component(facility.text)


            
        
    def write_facility_component(self, message):
        dir_name = './html_files/'
        file_name = datetime.today().strftime('%Y-%m-%d').replace("-","_") + "_" + self.state + ".txt"
        with open(dir_name + file_name, "a") as f:
            f.write(message + "\n\n")