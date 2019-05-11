## Game of Thrones easy login script
## 
## Description: This code logs into all of your fan sites automatically

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Firefox()
driver.implicitly_wait(5)
    ## implicity_wait makes the bot wait 5 seconds before every action
    ## so the site content can load up

# Define the functions

def login_to_westeros (username, userpass):

    ## Open the login page
    driver.get('https://asoiaf.westeros.org/index.php?/login/')    

    ## Log the details
    print(username + " is logging into westeros.")
    
    ## Find the fields and log into the account. 
    textfield_username = driver.find_element_by_id('auth')
    textfield_username.clear()
    textfield_username.send_keys(username)

    textfield_email = driver.find_element_by_id('password')
    textfield_email.clear()
    textfield_email.send_keys(userpass)

    submit_button = driver.find_element_by_id('elSignIn_submit')
    submit_button.click()

    ## Log the details
    print(username + " is logged in! -> westeros")



		
def login_to_reddit_freefolk (username, userpass):

    ## Open the login page
    driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2Fr%2Ffreefolk')    

    ## Log the details
    print(username + " is logging into /r/freefolk.")
    
    ## Find the fields and log into the account. 
    textfield_username = driver.find_element_by_id('loginUsername')
    textfield_username.clear()
    textfield_username.send_keys(username) 
    textfield_email = driver.find_element_by_id('loginPassword')
    textfield_email.clear()
    textfield_email.send_keys(userpass)

    submit_button = driver.find_element_by_class_name('AnimatedForm__submitButton')
    submit_button.click()

    ## Log the details
    print(username + " is logged in! -> /r/freefolk.")
    

## Define the user and email combo. 

login_to_westeros("gameofthronesfan86", PASSWORDHERE)

time.sleep(2)
driver.execute_script("window.open('');")
Window_List = driver.window_handles
driver.switch_to_window(Window_List[-1])

login_to_reddit_freefolk("MyManMance", PASSWORDHERE)

time.sleep(2)
driver.execute_script("window.open('');")
Window_List = driver.window_handles
driver.switch_to_window(Window_List[-1])


## wait for 2 seconds
time.sleep(2)


print("task complete")