from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Open login page
driver.get("https://www.saucedemo.com/")

# Username using By.ID
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# Password using By.NAME
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

# Login button using By.XPATH
login_button = driver.find_element(
    By.XPATH,
    "//input[@type='submit']"
)
login_button.click()

# Validate URL
assert "/inventory.html" in driver.current_url

print("Assignment 1 PASSED")
print("Current URL:", driver.current_url)

time.sleep(10)

driver.quit()  