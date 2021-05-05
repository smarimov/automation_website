from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
print('Open Website..')

driver.implicitly_wait(20)


def ordering_t_shirt():

    driver.get('http://automationpractice.com/index.php')

    women_menu = driver.find_element_by_link_text("Women")

    women_menu.click()

    more_info = driver.find_element_by_xpath(
        "//body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[2]/a[2]/span[1]")
    more_info.click()

    # drop down
    size_element = driver.find_element_by_id("group_1")
    drp_size = Select(size_element)
    drp_size.select_by_value('2')

    add_cart_button = driver.find_element_by_xpath(
        "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/form[1]/div[1]/div[3]/div[1]/p["
        "1]/button[1]")
    add_cart_button.click()

    checkout_button = driver.find_element_by_xpath(
        "//body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/a[1]/span[1]")

    checkout_button.click()

    proceed_checkout = driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/p[2]/a[1]/span[1]")
    proceed_checkout.click()

    # sign in

    email = driver.find_element_by_id("email")
    email.send_keys('mya@gmail.com')

    password = driver.find_element_by_id("passwd")
    password.send_keys('olim123#')
    driver.find_element_by_xpath('//*[@id="SubmitLogin"]').click()

    driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button').click()
    driver.find_element_by_xpath('//*[@id="cgv"]').click()

    driver.find_element_by_xpath('//*[@id="form"]/p/button').click()

    driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a').click()

    driver.find_element_by_xpath('//*[@id="cart_navigation"]/button').click()


ordering_t_shirt()
