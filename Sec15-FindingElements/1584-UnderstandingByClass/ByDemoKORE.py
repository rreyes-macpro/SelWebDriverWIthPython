from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):
        baseUrl = "https://jobs.jobvite.com/koretelematics"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        # elementById = driver.find_element(By.ID, "page-title")
        #
        # if elementById is not None:
        #     print("We found an element by Id")

        #The below code is designed for letskodeit practice page only

        # elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        #
        # if elementByXpath is not None:
        #     print("We found an element by XPATH")
        #
        elementByLinkText = driver.find_element(By.LINK_TEXT, "QA Test Analyst")

        if elementByLinkText is not None:
            print("We found an element by Link Text")
            print("The element by LinkText we found is \"" + str(elementByLinkText.text) + '"')

        #driver.close()

ff = ByDemo()
ff.test()