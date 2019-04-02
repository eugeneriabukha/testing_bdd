from selenium.webdriver.chrome.webdriver import WebDriver


def test_google_search():
    driver = WebDriver(executable_path='/home/stbt/py_works/testing_bdd/Drivers/chromedriver')
    driver.get('https://google.com.ua')
    search_input = driver.find_element_by_xpath('input.gLFyf.gsfi')
    print("")