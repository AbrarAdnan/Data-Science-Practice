from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def main():
    webdriver_path = r"C:\Users\Adnan\Desktop\Data Science\Week 3\chromedriver.exe"

    driver = webdriver.Chrome(webdriver_path)
    url = f"https://research.com/"
    driver.get(url)
    select_descipline = driver.find_element(By.ID, "select_discipline_scholars")
    all_options = select_descipline.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        if(option.text=="Computer Science"):
            option.click()
    select_country = driver.find_element(By.NAME, "countryCode")
    all_options = select_country.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        if(option.text=="United States"):
            option.click()
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/form/button")
    button.click()
    time.sleep(50)
    driver.close()



if __name__ == "__main__":
    main()