from selenium import webdriver
import os
import time

class RunSafariTests():
    # https://github.com/SeleniumHQ/selenium/wiki/SafariDriver
    # http://selenium-release.storage.googleapis.com/index.html

    def test(self):
        serverLocation = "/usr/local/bin/selenium-server-standalone-3.4.0.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation
        # Instantiate Safari Browser Command
        driver = webdriver.Safari(quiet=True)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")
        time.sleep(10)

safari = RunSafariTests()
safari.test()
