from selenium import webdriver
import os


class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "/usr/local/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")


ch = RunChromeTests()
ch.test()
