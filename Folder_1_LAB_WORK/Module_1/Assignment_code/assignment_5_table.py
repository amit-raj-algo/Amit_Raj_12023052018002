from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tables")

# Locate table
table = driver.find_element(By.ID, "table1")

# Get all rows
rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

target_name = "Smith"
found = False

# Iterate through rows
for row in rows:

    # Get columns in current row
    columns = row.find_elements(By.TAG_NAME, "td")

    # Print complete row
    row_data = [column.text for column in columns]

    print(row_data)

    # Find target name
    if target_name in columns[0].text:

        print("Target name found:", columns[0].text)

        # Corresponding value
        due_value = columns[3].text

        print("Corresponding value:", due_value)

        found = True
        break

assert found, "Target name was not found"

print("Assignment 5 PASSED")
time.sleep(10)

driver.quit()