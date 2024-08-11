from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=chrome_options)

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
chrome_browser.implicitly_wait(2)

show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOLLL')
show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')

assert 'I AM EXTRA COOLLL' in output_message.text

time.sleep(3)

chrome_browser.close()