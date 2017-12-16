from selenium import webdriver

class FindVariousElements():

    def testlink(self):
        baseurl = "https://jobs.jobvite.com/koretelematics"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        #partiallinktxt = "Kore Wireless Group"

        elementByClassName1 = driver.find_element_by_class_name("h2")
        ClassName1 = elementByClassName1.text
        # elementByID2 = driver.find_element_by_id("edit-search-block-form--2")
        # elementByID2.send_keys("kulafu")


        #elementByClass1 = driver.find_elements_by_class_name("search")
        #elementByLinkText1 = driver.find_element_by_partial_link_text(partiallinktxt)

        if elementByClassName1 is not None:
            print("Test Passed. We found an element by ID1 as 'Search' button")
            print(ClassName1) #it will list all the items in the dropbox
            for item in ClassName1:
                if item == 'Brochure':
                    print("Found item "+item+" in the list")
        else:
            print("Test Failed. No element by ID1 has been found")

        # if elementByID2 is not None:
        #     print("Test Passed. We found an element by ID2 as 'Search box'")
        #     print(elementByID2.text)
        # else:
        #     print("Test Failed. No element by ID2 has been found")
        #
        # if elementByClass1 is not None:
        #     print("Test Passed. We found a dropdown element by Class1 as 'Resource Type'")
        # else:
        #     print("Test Failed. No element by Class1 has been found")

        # if elementByLinkText1 is not None:
        #     #print("Test Passed. We found an element by Link as 'Register & Manage Your Employer Account'")
        #     print("Test Passed. We found an element by Link as '"+ partiallinktxt+"'")
        #     #print(elementByLinkText1.text)
        # else:
        #     print("Test Failed. No element by LinkText has been found")





ff = FindVariousElements()
ff.testlink()