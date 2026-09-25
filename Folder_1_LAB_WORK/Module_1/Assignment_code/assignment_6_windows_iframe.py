from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)



# PART 1: IFRAME


driver.get("https://the-internet.herokuapp.com/iframe")

# Wait for iframe
iframe = wait.until(
    EC.presence_of_element_located(
        (By.ID, "mce_0_ifr")
    )
)

# Switch into iframe
driver.switch_to.frame(iframe)

print("Switched into iframe")

# Find content inside iframe
body = driver.find_element(By.TAG_NAME, "body")

print("Iframe text:", body.text)

# Return to main document
driver.switch_to.default_content()

print("Returned to main page")



# PART 2: NEW WINDOW / TAB


driver.get("https://the-internet.herokuapp.com/windows")

# Save main window handle
main_window = driver.current_window_handle

print("Main window:", main_window)

# Click link that opens new window
wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Click Here")
    )
).click()

# Get all windows
handles = driver.window_handles

print("Number of windows:", len(handles))

# Switch to new window
for handle in handles:

    if handle != main_window:

        driver.switch_to.window(handle)

        break

# New window title
print("New window title:", driver.title)

# Close new window
driver.close()

print("New window closed")

# Switch back to main window
driver.switch_to.window(main_window)

print("Back to main window")

print("Assignment 6 PASSED")

time.sleep(10)

driver.quit()