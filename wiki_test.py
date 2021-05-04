from selenium import webdriver
from selenium.webdriver import ActionChains

from locators import *


class WikiTest:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/Metis_(mythology)"
        self.driver = webdriver.Chrome("chromedriver")

    def a_test(self):
        # Verifying Context box list of heading names are matching with actual header names
        self.driver.get(self.url)
        content_family = self.driver.find_element_by_xpath(LIST_OF_CONTENTS_FAMILY).text
        header_family = self.driver.find_element_by_xpath(FAMILY_HEADING).text
        if content_family == header_family:
            print('Pass')
        else:
            print('Fail')

        content_myth = self.driver.find_element_by_xpath(LIST_OF_CONTENTS_MYTHOLOGY).text
        header_myth = self.driver.find_element_by_xpath(MYTHOLOGY_HEADING).text
        if content_myth == header_myth:
            print('Pass')
        else:
            print('Fail')

        content_soc = self.driver.find_element_by_xpath(LIST_OF_CONTENTS_SOCIOLOGY).text
        header_soc = self.driver.find_element_by_xpath(SOCIOLOGY_HEADING).text
        if content_soc == header_soc:
            print('Pass')
        else:
            print('Fail')

        content_hon = self.driver.find_element_by_xpath(LIST_OF_CONTENTS_HONOURS).text
        header_hon = self.driver.find_element_by_xpath(HONOURS_HEADING).text
        if content_hon == header_hon:
            print('Pass')
        else:
            print('Fail')

        content_ref = self.driver.find_element_by_xpath(LIST_OF_CONTENTS_REFERENCES).text
        header_ref = self.driver.find_element_by_xpath(REFERENCES_HEADING).text
        if content_ref == header_ref:
            print('Pass')
        else:
            print('Fail')

        content_read = self.driver.find_element_by_xpath(LIST_OF_CONTENTS_READING).text
        header_read = self.driver.find_element_by_xpath(READING_HEADING).text
        if content_read == header_read:
            print('Pass')
        else:
            print('Fail')
        self.driver.quit()

    def b_test(self):
        self.driver.get(self.url)
        hyperlink_fam = self.driver.find_element_by_xpath(HYPERLINK_FAMILY).get_attribute('href')
        if 'https://en.wikipedia.org/wiki/Metis_(mythology)#Family' == hyperlink_fam:
            print('Pass')
        else:
            print('Fail')

        hyperlink_fam = self.driver.find_element_by_xpath(HYPERLINK_MYTHOLOGY).get_attribute('href')
        if 'https://en.wikipedia.org/wiki/Metis_(mythology)#Mythology' == hyperlink_fam:
            print('Pass')
        else:
            print('Fail')

        hyperlink_fam = self.driver.find_element_by_xpath(HYPERLINK_SOCIOLOGY).get_attribute('href')
        if 'https://en.wikipedia.org/wiki/Metis_(mythology)#In_sociology' == hyperlink_fam:
            print('Pass')
        else:
            print('Fail')

        hyperlink_fam = self.driver.find_element_by_xpath(HYPERLINK_HONOURS).get_attribute('href')
        if 'https://en.wikipedia.org/wiki/Metis_(mythology)#Honours' == hyperlink_fam:
            print('Pass')
        else:
            print('Fail')

        hyperlink_fam = self.driver.find_element_by_xpath(HYPERLINK_REFERENCES).get_attribute('href')
        if 'https://en.wikipedia.org/wiki/Metis_(mythology)#References' == hyperlink_fam:
            print('Pass')
        else:
            print('Fail')

        hyperlink_fam = self.driver.find_element_by_xpath(HYPERLINK_READING).get_attribute('href')
        if 'https://en.wikipedia.org/wiki/Metis_(mythology)#Further_reading' == hyperlink_fam:
            print('Pass')
        else:
            print('Fail')
        self.driver.quit()

    def c_test(self):
        self.driver.get(self.url)
        ho = self.driver.find_element_by_xpath(NIKE_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", ho)
        hover = ActionChains(self.driver)
        hover.move_to_element(ho).perform()
        text = self.driver.find_element_by_xpath(POPUP_TEXT).text
        print(text)
        if text == "In ancient Greek civilization, Nike was a goddess who personified victory. Her Roman equivalent was Victoria.":
            print('Pass')
        else:
            print('Fail')

        self.driver.quit()

    def d_test(self):
        self.driver.get(self.url)
        self.driver.find_element_by_xpath(NIKE_LINK).click()
        ho = self.driver.find_element_by_xpath(FAMILY_TREE)
        self.driver.execute_script("arguments[0].scrollIntoView();", ho)
        if ho.text == 'Family tree':
            print('Pass')
        else:
            print('Fail')
        self.driver.quit()


run = WikiTest()
run.a_test()
run.b_test()
# run.c_test()
run.d_test()
