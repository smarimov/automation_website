from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.implicitly_wait(20)
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