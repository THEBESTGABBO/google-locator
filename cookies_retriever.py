# %%
# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from netscape_cookies import save_cookies_to_file

# Setup Chrome options to 
    #Disable the "enable-automation" flag.
    #Add the "no-sandbox" argument.
    #Add the "disable-infobars" argument.
    #Add the "disable-dev-shm-usage" argument.

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set the driver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)


def login(username, password):
    #navigate to login gmail
    driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")

    # Identify the user name text box and enter the value
    driver.find_element(By.ID, "identifierId").send_keys(username)
    time.sleep(1)

    # Clicks on the 'Next' button and waits for 2 seconds.
    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    time.sleep(5)

    driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys(password)
    time.sleep(2)

    # Clicks on the 'Next' button again and waits for 2 seconds.
    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    time.sleep(2)

def retrieveCookiesFromGoogle(username, password, google_url="https://www.google.com/maps"):
    login(username, password)
    driver.get(google_url)
    cookie_data=driver.get_cookies()

    file_path = "cookies.txt"

    # Save cookies to file in Netscape format
    save_cookies_to_file(cookie_data, file_path)

#Uncomment below code to close the browser  
driver.close()
