from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

driver = webdriver.Chrome()

try:
    driver.get("file:///D:/D_Drive_Data/SIT(CSE)/DevOps/selenium/Student-Feedback-Form/index.html")

    print("Page Title:", driver.title)

    wait = WebDriverWait(driver, 10)

    # Fill form
    wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@gmail.com")
    driver.find_element(By.ID, "mobile").send_keys("9876543210")
    driver.find_element(By.ID, "department").send_keys("CSE")
    driver.find_element(By.XPATH, "//input[@value='Male']").click()

    driver.find_element(By.ID, "feedback").send_keys(
        "This is a very good platform for learning and gaining knowledge effectively"
    )

    # Submit
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Handle alert
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert message:", alert.text)
    alert.accept()

    # Wait and re-find reset button
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='reset']")))

    driver.find_element(By.XPATH, "//button[@type='reset']").click()

    print("Test Completed Successfully")
    sys.exit(0)

except Exception as e:
    print("Test Failed:", e)
    sys.exit(1)

finally:
    driver.quit()