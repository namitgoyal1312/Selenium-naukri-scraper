from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.google.com")
print("Page title:", driver.title)

# Keep the browser open for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()