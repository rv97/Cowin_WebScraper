from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import re
from utils import Cowinutils
import constants
class CowinParser():

    def __init__(self):
        self.start_time = time.time()
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.cowin.gov.in/home")
        time.sleep(3)

    def setStateAndDistrictInWeb(self):
        stateName, districtName = self.cowin_utils.getStateAndDistrictName()
        self.driver.find_element_by_class_name("status-switch").click()
        time.sleep(1)
        stateBox = self.driver.find_element_by_xpath(constants.STATE_BOX_XPATH)
        time.sleep(0.3)
        stateBox.click()
        time.sleep(0.5)
        stateBox.send_keys(stateName)
        time.sleep(0.5)
        stateBox.send_keys(Keys.ENTER)
        districtBox = self.driver.find_element_by_xpath(constants.DISTRICT_BOX_XPATH)
        time.sleep(0.3)
        districtBox.click()
        time.sleep(0.5)
        districtBox.send_keys(districtName)
        time.sleep(0.5)
        districtBox.send_keys(Keys.ENTER)
        time.sleep(0.5)
        self.clickOnSearch()

    def clickOnSearch(self):
        self.driver.find_element_by_xpath(constants.SEARCH_BUTTON_XPATH).click()
        time.sleep(3)
        self.selectFilters()

    def selectFilters(self):
        filterButtons = self.driver.find_elements_by_class_name(constants.FILTERS_CLASSNAME)
        userFilters = self.cowin_utils.getQueryDettails()['filters']
        for filterButton in filterButtons:
            if filterButton.text in userFilters:
                filterButton.click()
                time.sleep(0.3)
        self.getRows()
                
    def getRows(self):
        rows = self.driver.find_elements_by_css_selector(constants.ROWS_CSS_SELECTOR)
        for row in rows:
            row_text = row.text
            row_split = row_text.split("\n")
            isSlotAvailable = self.isSlotAvailable(row_split)
            if isSlotAvailable:
                print(row_split[0])
        print("--- %s seconds ---" % (time.time() - self.start_time))

    def isSlotAvailable(self, row_split):
        for index in range(2, len(row_split)):
            isAvailable = re.search(constants.AVAILABILITY_REGEX, row_split[index])
            if isAvailable:
                return isAvailable
    
    def startProcess(self, queryParameters):
        self.cowin_utils = Cowinutils()
        self.cowin_utils.setQueryDetails(queryParameters)
        self.cowin_utils.getListOfStatesAndDistrict()
        self.setStateAndDistrictInWeb()
        self.driver.quit()

# cowinParser = CowinParser()
