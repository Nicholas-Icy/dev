from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Set up driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Get absolute path to login.html
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
file_path = "file://" + os.path.join(current_dir, "login.html")
print(file_path)
driver.get(file_path)

# TC_001 - Valid Login
driver.find_element(By.ID, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "password").send_keys("Test@123")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(1)
msg = driver.find_element(By.ID, "message").text
print("TC_001 Valid Login:", "PASS" if "Successful" in msg else "FAIL")

# TC_002 - Wrong Password
driver.find_element(By.ID, "email").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "password").send_keys("WrongPass")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(1)
msg = driver.find_element(By.ID, "message").text
print("TC_002 Wrong Password:", "PASS" if "Invalid" in msg else "FAIL")

# TC_003 - Empty Fields
driver.find_element(By.ID, "email").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "loginBtn").click()
time.sleep(1)
msg = driver.find_element(By.ID, "message").text
print("TC_003 Empty Fields:", "PASS" if "cannot be empty" in msg else "FAIL")

driver.quit()