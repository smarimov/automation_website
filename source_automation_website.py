import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)


def send_message():
    driver.get('http://automationpractice.com/index.php')

    contact_us_menu = driver.find_element_by_link_text('Contact us')
    contact_us_menu.click()

    subject_heading_element = driver.find_element_by_id('id_contact')
    drp = Select(subject_heading_element)
    drp.select_by_index('1')

    email_input = driver.find_element_by_id('email')
    email_input.send_keys('mya@gmail.com')

    order_reference = driver.find_element_by_name('id_order')
    order_reference.send_keys('15')

    attach_file = driver.find_element_by_id('fileUpload')
    path = '/screenshot_ecommerce/blouses_page.png'
    attach_file.send_keys(path)

    message_input = driver.find_element_by_id('message')
    message_input.send_keys('The following screenshot is very blurry. Could you work on that.')

    time.sleep(2)

    submit = driver.find_element_by_id('submitMessage')
    submit.click()


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


def slider_automation():
    driver.get('http://automationpractice.com/index.php')
    forward = driver.find_element_by_xpath('//a[@class="bx-next"]')
    forward.click()


def mouse_navigation():
    driver.get('http://automationpractice.com/index.php')
    women_menu = driver.find_element_by_xpath('//a[@title="Women"]')

    blouses = driver.find_element_by_xpath('//a[@title="Blouses"]')

    mouse_actions = ActionChains(driver)
    mouse_actions.move_to_element(women_menu).move_to_element(blouses).click().perform()

    driver.get_screenshot_as_file('C:\\dev\\automation_website\\screenshot_ecommerce\\blouses_page.png')

    discover_button = driver.find_element_by_link_text('Discover our stores')
    discover_button.click()

    ok_button = driver.find_element_by_xpath('//button[@class="dismissButton"]').click()

    address_input = driver.find_element_by_id('addressInput')
    address_input.send_keys('Pittsburgh')

    element = driver.find_element_by_id('radiusSelect')

    drp = Select(element)
    drp.select_by_value('100')

    search_button = driver.find_element_by_name('search_locations')
    search_button.click()

    close_pop_up = driver.find_element_by_xpath('//a[@title="Close"]')
    close_pop_up.click()


