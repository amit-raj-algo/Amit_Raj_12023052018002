from selenium import webdriver


def before_all(context):

    print("\nStarting Chrome browser...")

    context.driver = webdriver.Chrome()

    context.driver.maximize_window()


def after_all(context):

    print("\nClosing Chrome browser...")

    if hasattr(context, "driver"):
        context.driver.quit()
        