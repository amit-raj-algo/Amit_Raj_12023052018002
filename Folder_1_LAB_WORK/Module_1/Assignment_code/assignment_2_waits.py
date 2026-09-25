from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Open dynamic loading page
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Click Start
start_button = driver.find_element(
    By.CSS_SELECTOR,
    "#start button"
)
start_button.click()

# Explicit wait
wait = WebDriverWait(driver, 10)

# Wait until Hello World becomes visible
finish_element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "finish")
    )
)

# Extract text
text = finish_element.text

print("Extracted text:", text)

# Validation
assert text == "Hello World!"

print("Assignment 2 PASSED")

driver.quit()