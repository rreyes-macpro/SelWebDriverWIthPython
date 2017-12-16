from selenium import webdriver

class RunFFTests():

    def test(self):
        # Instantiate FF Browser Command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get("http://www.koretelematics.com")
        driver.close()
        print("Browser has been closed")

ff = RunFFTests()
ff.test()
