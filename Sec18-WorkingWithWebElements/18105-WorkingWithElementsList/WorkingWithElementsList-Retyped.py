from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WorkingWithElementsList():

    def TestListOfElements(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)


        radBtnLst = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radBtnLst)
        print("Size of the list is : " + str(size))


        for radbtn in radBtnLst:
            isSelected = radbtn.is_selected()

            if not isSelected:
                radbtn.click()
                time.sleep(2)

ff = WorkingWithElementsList()
ff.TestListOfElements()

