from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():
    # Configure Chrome options to hide the "automated software" notification bar
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Setup Chrome driver using webdriver-manager and pass options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open a test website
        driver.get("https://www.udemy.com")
        print(f"Page title is: {driver.title}")
        time.sleep(2)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
