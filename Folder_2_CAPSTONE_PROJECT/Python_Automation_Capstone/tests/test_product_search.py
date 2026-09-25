from pages.product_page import ProductPage
from utils.csv_reader import CSVReader


def test_product_search(driver):
    print("\n========================================")
    print("      PRODUCT SEARCH AUTOMATION TEST")
    print("========================================")

    print("[1] Reading product data from CSV...")
    test_data = CSVReader.read_test_data()[0]
    print(f"[PASS] Product loaded: {test_data['product']}")

    print("[2] Opening application...")
    product_page = ProductPage(driver)
    print("[PASS] Application opened")

    print("[3] Searching for product...")
    product_page.search_product(test_data["product"])
    print(f"[PASS] Search performed for: {test_data['product']}")

    print("[4] Verifying search result...")
    assert test_data["product"] in driver.page_source
    print("[PASS] Product found in search results")

    print("========================================")
    print("      PRODUCT SEARCH TEST PASSED")
    print("========================================\n")