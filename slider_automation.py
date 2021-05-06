from selenium import webdriver

driver = webdriver.Chrome()


def slider_automation():
    driver.get('http://automationpractice.com/index.php')
    forward = driver.find_element_by_xpath('//a[@class="bx-next"]')
    forward.click()
