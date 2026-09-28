import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_data = [
    {"skills": "Python Developer", "exp": "2 years", "location": "Bangalore"},
    {"skills": "QA Automation", "exp": "3 years", "location": "Gurugram"},
    {"skills": "Data Analyst", "exp": "1 year", "location": "Delhi / NCR"}
]
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)


for data in test_data:
        print(f"\nSearching for: {data['skills']} | {data['exp']} | {data['location']}")
        
        driver.get("https://www.naukri.com/")

        
        skill_field = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@placeholder, 'Enter skills') or contains(@class, 'suggestor-input')]")
        ))
        skill_field.click()
        skill_field.clear()
        skill_field.send_keys(data["skills"])

        
        exp_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(@placeholder, 'Select experience') or contains(text(), 'Select experience') or contains(@id, 'expWD')]")
        ))
        exp_dropdown.click()

        
        exp_opt = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[contains(text(), '{data['exp']}')]")
        ))
        exp_opt.click()

       
        loc_field = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@placeholder, 'Enter location')]")
        ))
        loc_field.click()
        loc_field.clear()
        loc_field.send_keys(data["location"])

        
        search_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'qsbSubmit')]")
        ))
        search_btn.click()
        
driver.quit()