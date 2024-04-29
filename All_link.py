from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service=webdriver.chrome.service.Service("chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.ycombinator.com/companies")

select_all=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div/div[10]/a")))

#Extracting The Xpath of each checkboxes in batches column
batches=[]
for i in range(2,41):
    path="/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div/div[10]/div["+str(i)+"]/label/input"
    batches.append(path)

for batch in batches:
    select=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,batch)))
    select.click()

    time.sleep(7)

    def extract_hrefs_from_column(xpath):
            service = Service('chromedriver.exe')
            driver = webdriver.Chrome(service=service)
            driver.get("https://www.ycombinator.com/companies")


            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))


            def scroll_to_bottom():
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    time.sleep(2)

            scroll_to_bottom()


            elements = driver.find_elements(By.XPATH, xpath)


            while True:

                    scroll_to_bottom()
                    new_elements = driver.find_elements(By.XPATH, xpath)
                    if len(new_elements) == len(elements):
                            break
                    elements = new_elements


            hrefs = [element.get_attribute("href") for element in elements]


            driver.quit()

            return hrefs

    #Unticking the selected checkbox
    select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, batch)))
    select.click()


    def save_links_to_txt(hrefs):
            with open("company_links.txt", "a") as f:
                    for href in hrefs:
                            f.write(f"{href}\n")


    column_xpath = "//a[@class='_company_99gj3_339']"
    hrefs = extract_hrefs_from_column(column_xpath)

    # Save the extracted hrefs to a text file
    save_links_to_txt(hrefs)
