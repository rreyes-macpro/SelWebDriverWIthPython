from selenium import webdriver

class FindVariousElements():

    def testlink(self):
        baseurl = "https://www.wcb.mb.ca"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        linktxt = "Register & Manage Your Employer Account"

        elementByID1 = driver.find_element_by_id("quicklinks_resource_type")
        id1 = elementByID1.text
        elementByID2 = driver.find_element_by_id("edit-search-block-form--2")
        elementByID2.send_keys("kulafu")


        elementByClass1 = driver.find_elements_by_class_name("search")
        elementByLinkText1 = driver.find_element_by_link_text(linktxt)

        if elementByID1 is not None:
            print("Test Passed. We found an element by ID1 as 'Search' button")
            print(id1) #it will list all the items in the dropbox
            for item in id1:
                if item == 'Brochure':
                    print("Found item "+item+" in the list")
        else:
            print("Test Failed. No element by ID1 has been found")

        if elementByID2 is not None:
            print("Test Passed. We found an element by ID2 as 'Search box'")
            print(elementByID2.text)
        else:
            print("Test Failed. No element by ID2 has been found")

        if elementByClass1 is not None:
            print("Test Passed. We found a dropdown element by Class1 as 'Resource Type'")
        else:
            print("Test Failed. No element by Class1 has been found")

        if elementByLinkText1 is not None:
            #print("Test Passed. We found an element by Link as 'Register & Manage Your Employer Account'")
            print("Test Passed. We found an element by Link as '"+ linktxt+"'")
            #print(elementByLinkText1.text)
        else:
            print("Test Failed. No element by LinkText has been found")





ff = FindVariousElements()
ff.testlink()