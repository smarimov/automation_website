import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

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
path = 'C:\\dev\\automation_website\\screenshot_ecommerce\\blouses_page.png'
attach_file.send_keys(path)

message_input = driver.find_element_by_id('message')
message_input.send_keys('The following screenshot is very blurry. Could you work on that.')

time.sleep(2)

submit = driver.find_element_by_id('submitMessage')
submit.click()
