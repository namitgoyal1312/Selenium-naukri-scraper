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
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

all_results = []

try:
    for data in test_data:
        
      
        driver.get("https://www.naukri.com/")
        time.sleep(2)

        
        skill_field = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@placeholder, 'Enter skills')]")
        ))
        skill_field.click()
        skill_field.clear()
        skill_field.send_keys(data["skills"])

        
        exp_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[, 'Select experience')]")
        ))
        exp_dropdown.click()
        time.sleep(1)

        
        exp_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"")
        ))
        exp_option.click()

        
        loc_field = wait.until(EC.element_to_be_clickable(
            (By.XPATH, ", 'Enter location')]")
        ))
        loc_field.click()
        loc_field.clear()
        loc_field.send_keys(data["location"])

        
        search_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "")
        ))
        # JavaScript click handles overlays or sticky headers reliably
        driver.execute_script("arguments[0].click();", search_btn)

       
        time.sleep(4)  # Allow results to render
        job_cards = driver.find_elements(By.CSS_SELECTOR, "div.srp-jobtuple-wrapper, article.jobTuple")

        if not job_cards:
            print("No jobs found for this criteria.")
        else:
            # Capture up to top 5 job listings
            for card in job_cards[:5]:
                try:
                    title = card.find_element(By.CSS_SELECTOR, "a.title").text
                except:
                    title = "N/A"
                try:
                    company = card.find_element(By.CSS_SELECTOR, "a.comp-name, a.subTitle").text
                except:
                    company = "N/A"

                all_results.append({
                    "Skill Query": data["skills"],
                    "Exp Query": data["exp"],
                    "Location Query": data["location"],
                    "Job Title": title,
                    "Company": company
                })

finally:
    driver.quit()