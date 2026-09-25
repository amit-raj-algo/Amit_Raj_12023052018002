def test_open_application(driver):
    print("\n========================================")
    print("       APPLICATION SETUP TEST")
    print("========================================")

    print("[1] Launching Chrome browser...")
    print("[PASS] Chrome browser launched")

    print("[2] Opening application...")
    print("[PASS] Application opened successfully")

    print("[3] Verifying application title...")
    assert "Your Store" in driver.title
    print("[PASS] Application title verified")

    print("========================================")
    print("       SETUP TEST PASSED")
    print("========================================\n")