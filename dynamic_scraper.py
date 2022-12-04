from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

columns = ['Conference Names', "Time Remaining", "Date" ,"Note", "Conference Deadline", "Category"]

def get_conference(conf):
    details = conf.text.split('\n')
    content = {}
    content['Conference Names'] = details[0]
    content['Time Remaining'] = details[1]
    content['Date'] = details[2]
    if(details[3].split()[0]=="Deadline:"):
        content['Conference Deadline'] = details[3]
        content['Note'] = "No notes available"
    if(details[3].split()[0]=="Note:"):
        content['Note'] = details[3]
        content['Conference Deadline'] = details[4]
    content['Category'] = details[len(details)-1]
    return content


def main():
    webdriver_path = r"C:\Users\Adnan\Desktop\Data Science\Week 3\chromedriver.exe"

    driver = webdriver.Chrome(webdriver_path)
    url = f"https://aideadlin.es/?sub=ML,CV,CG,NLP,RO,SP,DM,AP,KR"
    driver.get(url)
    coming_confs = driver.find_element(By.ID, "coming_confs")
    rows = coming_confs.find_elements(By.CLASS_NAME, "ConfItem")
    conference_data = []
    for conf in rows:
        conference_data.append(get_conference(conf))
    #time.sleep(10)
    driver.close()

    df = pd.DataFrame(conference_data,columns=columns)
    print(df)



if __name__ == "__main__":
    main()