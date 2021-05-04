from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver.exe")


def open_website():
    driver.get('http://automationpractice.com/index.php')
    driver.implicitly_wait(20)


def sign_in_button():
    # find 'sign in' element and click on it:
    sign_in = driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")
    sign_in.click()


def person_info_input(email_1, title_1, f_name, l_name, pass_word, day, month, year, home_address, current_city, state,
                      zipcode, country, phone_number):
    # write your email and click on 'create account':
    email_input = driver.find_element_by_id('email_create')
    email_input.send_keys(email_1)
    create_account_button = driver.find_element_by_name('SubmitCreate')
    create_account_button.click()

    # write personal information:
    title = title_1.title()
    if title == "Mr.":
        driver.find_element_by_name('id_gender').click()
    elif title == "Mrs.":
        driver.find_element_by_id("id_gender2").click()

    first_name = driver.find_element_by_id('customer_firstname')
    first_name.send_keys(f_name)

    last_name = driver.find_element_by_id('customer_lastname')
    last_name.send_keys(l_name)

    password = driver.find_element_by_id('passwd')
    password.send_keys(pass_word)

    # dropdown days
    element_days = driver.find_element_by_xpath("//select[@id='days']")
    drp_days = Select(element_days)
    drp_days.select_by_value(day)

    # dropdown month
    element_months = driver.find_element_by_id('months')
    drp_months = Select(element_months)
    drp_months.select_by_value(month)

    # dropdown years
    element_years = driver.find_element_by_id('years')
    drp_years = Select(element_years)
    drp_years.select_by_value(year)

    address = driver.find_element_by_id('address1')
    address.send_keys(home_address)

    city = driver.find_element_by_id('city')
    city.send_keys(current_city)

    # dropdown state:
    element_state = driver.find_element_by_id('id_state')
    drp_state = Select(element_state)
    drp_state.select_by_value(state)

    zip_code = driver.find_element_by_id('postcode')
    zip_code.send_keys(zipcode)

    # dropdown country:
    element_country = driver.find_element_by_id('id_country')
    drp_country = Select(element_country)
    drp_country.select_by_value(country)

    phone = driver.find_element_by_id('phone_mobile')
    phone.send_keys(phone_number)


def register_button():
    register = driver.find_element_by_xpath("//button[@id='submitAccount']")
    register.click()


open_website()


def send_message():
    contactus_button = driver.find_element_by_link_text("Contact us")
    contactus_button.click()

    # dropdown
    element_subject = driver.find_element_by_id("id_contact")

    drp_subject = Select(element_subject)

    drp_subject.select_by_value('2')

    email = driver.find_element_by_id("email")
    email.send_keys('mya@gmail.com')

    order_number = driver.find_element_by_id("id_order")
    order_number.send_keys('154678')

    # uploading file
    path = "C:\\Users\\shoki\\OneDrive\\Desktop\\New Text Document.txt"

    element_upload = driver.find_element_by_id("fileUpload")
    element_upload.send_keys(path)

    message_input = driver.find_element_by_id("message")
    message_input.send_keys("I did not receive my order")

    send_button = driver.find_element_by_xpath("//button[@id='submitMessage']")
    send_button.click()
