from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import requests
import time
import re

class CowinParser():

    def __init__(self):
        self.start_time = time.time()
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.cowin.gov.in/home")
        time.sleep(3)
        self.getStates()
        
    def getStates(self):
        REQUEST_URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        self.headers={
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        result = requests.get(REQUEST_URL, headers=self.headers)
        self.STATES_JSON = result.json()
        print("Select the State Number: ")
        for state in self.STATES_JSON['states']:
            print(str(state['state_id'])+" "+state['state_name'])
        stateNumber = input()
        stateNumber = int(stateNumber)
        self.getDistrict(stateNumber)

    def getDistrict(self, stateNumber):
        REQUEST_URL = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(stateNumber)
        result = requests.get(REQUEST_URL, headers=self.headers)
        self.DISTRICTS = result.json()
        for district in self.DISTRICTS['districts']:
            print(str(district['district_id'])+" "+district['district_name'])
        districtNumber = input()
        districtNumber = int(districtNumber)
        self.setStateAndDistrictInWeb(stateNumber, districtNumber)

    def getStateAndDistrictName(self, stateNumber, districtNumber):
        stateName = self.STATES_JSON['states'][stateNumber]['state_name']
        for district in self.DISTRICTS['districts']:
            if district['district_id'] == districtNumber:
                districtName = district['district_name']
        return stateName, districtName

    def setStateAndDistrictInWeb(self, stateNumber, districtNumber):
        stateName, districtName = self.getStateAndDistrictName(stateNumber, districtNumber)
        self.driver.find_element_by_class_name("status-switch").click()
        time.sleep(1)
        stateBox = self.driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[1]/mat-form-field/div/div[1]/div/mat-select")
        stateBox.click()
        time.sleep(0.5)
        stateBox.send_keys(stateName)
        time.sleep(0.5)
        stateBox.send_keys(Keys.ENTER)
        time.sleep(0.5)
        districtBox = self.driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[2]/mat-form-field/div/div[1]/div/mat-select")
        districtBox.click()
        time.sleep(0.5)
        districtBox.send_keys(districtName)
        time.sleep(0.5)
        districtBox.send_keys(Keys.ENTER)
        time.sleep(0.5)
        self.clickOnSearch()

    def clickOnSearch(self):
        self.driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[3]/button").click()
        time.sleep(3)
        self.selectFilters()

    def selectFilters(self):
        filterButtons = self.driver.find_elements_by_class_name("form-check-label")
        for filterButton in filterButtons:
            if filterButton.text == "Age 45+" or filterButton.text == "Covishield" or filterButton.text == "Covaxin":
                filterButton.click()
                time.sleep(0.3)
        self.getRows()
                
    def getRows(self):
        rows = self.driver.find_elements_by_css_selector("[class='row ng-star-inserted']")
        for row in rows:
            row_text = row.text
            row_split = row_text.split("\n")
            isSlotAvailable = self.isSlotAvailable(row_split)
            if isSlotAvailable:
                print(row_split[0])
        print("--- %s seconds ---" % (time.time() - self.start_time))

    def isSlotAvailable(self, row_split):
        for index in range(2, len(row_split)):
            isAvailable = re.search("^[0-9]", row_split[index])
            if isAvailable:
                return isAvailable

cowinParser = CowinParser()
