from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

wait = WebDriverWait(driver, 10)

# -----------------------------
# PART 1: CHECKBOX
# -----------------------------

checkbox = wait.until(
    EC.presence_of_element_located(
        (By.ID, "ctl00_mainContent_chk_friendsandfamily")
    )
)

if not checkbox.is_selected():
    checkbox.click()

assert checkbox.is_selected()

print("Checkbox selected successfully")


# -----------------------------
# PART 2: AUTO-SUGGEST
# -----------------------------

auto_input = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "autosuggest")
    )
)

auto_input.send_keys("ind")

# Wait for suggestions
options = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
    )
)

# Loop through suggestions
found = False

for option in options:

    text = option.text.strip()

    print("Suggestion:", text)

    if text.lower() == "india":
        option.click()
        found = True
        break

assert found, "India option was not found"

print("Auto-suggest option selected successfully")
print("Assignment 3 PASSED")

driver.quit()