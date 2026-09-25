from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

wait = WebDriverWait(driver, 10)


# 1. JAVASCRIPT ALERT


alert_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Alert']")
    )
)

alert_button.click()

alert = wait.until(EC.alert_is_present())

print("Alert text:", alert.text)

alert.accept()

print("First alert accepted")



# 2. CONFIRM BOX


confirm_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Confirm']")
    )
)

confirm_button.click()

alert = wait.until(EC.alert_is_present())

print("Confirm text:", alert.text)

# Dismiss = Cancel
alert.dismiss()

print("Confirm dismissed")



# 3. PROMPT BOX


prompt_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Prompt']")
    )
)

prompt_button.click()

alert = wait.until(EC.alert_is_present())

print("Prompt text:", alert.text)

# Enter text
alert.send_keys("Amit")

# Submit prompt
alert.accept()

print("Prompt submitted")

print("Assignment 4 PASSED")

driver.quit()