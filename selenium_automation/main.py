from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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
        driver.maximize_window()
        # driver.get("https://www.udemy.com")
        driver.get("https://demoqa.com/automation-practice-form")
        print(f"Page title is: {driver.title}")
        print(f"type of title is  :{type(driver.title)}")
        print(f"Page URL: {driver.current_url}")
        # print(f"Page source: {driver.page_source}")

        # This will wait UP TO 10 seconds for an element to appear
        # It stops waiting the millisecond the element is found
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "submit"))
        )
        print(submit_button)
        print(submit_button.text)
        print(f"type of submit button is  :{type(submit_button)}")
        print(
            f"submit button innerHTml is : {submit_button.get_attribute('innerHTML')}"
        )
        print(
            f"type of innerHtml is : {type(submit_button.get_attribute('innerHTML'))}"
        )

        # 2. Use find_element for everything else (it's much faster/cleaner)
        first_name = driver.find_element(By.ID, "firstName")
        first_name.send_keys("Jatin")

        last_name = driver.find_element(By.ID, "lastName")
        last_name.send_keys("Goyal")

        # To clear an existing value before typing
        email = driver.find_element(By.ID, "userEmail")
        email.clear()
        email.send_keys("testing@example.com")
        print(f"email value: {email.get_attribute('value')}")
        time.sleep(2)
        # Clearing the field after typing
        email.send_keys(Keys.CONTROL + "a")  # Highlight everything
        email.send_keys(Keys.BACK_SPACE)  # Delete it
        print(f"email value after cleaning the field: {email.get_attribute('value')}")
        print(f"type of email is  :{type(email)}")
        submit_button.click()
        time.sleep(5)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
