## Selenium Log In Test
## 
## Description: This code logs into https://imgur.com automatically using Firefox.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

## Define which browser to use
driver = webdriver.Firefox()
driver.implicitly_wait(5)
## implicity_wait makes the bot wait 5 seconds before every action
## so the site content can load up

## Define the user and email combo. 
bot_name = 'testingwithselenium'
bot_email = bot_name + '@gmail.com'
bot_password = 'testingwithselenium1' ## required a number, so 1 is at the end
print(bot_name + " is getting started")

## Open the login page
driver.get('https://imgur.com/signin')

## This code checks the page for specific HTML tags
## This is looking for the element with ID 'username'			
textfield_username = driver.find_element_by_id('username')
textfield_username.clear()
textfield_username.send_keys(bot_email)

## This is looking for the element with ID 'password'			
textfield_email = driver.find_element_by_id('password')
textfield_email.clear()
textfield_email.send_keys(bot_password)

## This is looking for the element with the class 'btn_action'			
submit_button = driver.find_element_by_class_name('btn-action')
submit_button.click()

## wait for 2 seconds
time.sleep(2)

## RESULT == it should log you in

## Now to close the browser
try:
    print(bot_name + "closing")
finally:
    driver.quit()
    

print("task complete")