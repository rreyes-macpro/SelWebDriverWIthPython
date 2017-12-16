from selenium import webdriver

class BrowserInteractions():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice" # variable baseURL
        driver = webdriver.Firefox() #setting the webdriver firefox into 'driver' variable

        # Window Maximize
        driver.maximize_window() #this command opens a blank webpage as per driver and maximize it

        # Open the Url
        driver.get(baseUrl) #then it will get the URL/website as per baseURL

        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)

        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")

        # Open another Url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Browser Back (Going 1 step backward in the browser history)
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Browser Forward (Going 1 step forward in the browser history)
        driver.forward()
        print("Go one step forward in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Get Page Source
        pageSource = driver.page_source
        #print(pageSource)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

ff = BrowserInteractions()
ff.test()