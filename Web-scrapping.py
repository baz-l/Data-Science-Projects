import json
import threading
from queue import Queue
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Function to extract data from a single website
def extract_data_from_website(url):
    chrome_options = Options()
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--headless")
    service = webdriver.chrome.service.Service('chromedriver.exe')  # importing the service
    driver = webdriver.Chrome(service=service,options=chrome_options)  # assigning the service
    driver.get(url)  # Use the passed URL instead of hardcoded one

    # Initialize industry tags for each website
    industry_tags = []

    name_element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@class='font-extralight']")))
    name = name_element.text.strip()

    try:
        tagline_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'text-xl')))
        tagline = tagline_element.text.strip()
    except Exception as e:
        tagline = None

    try:
        descrption_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/section/div[2]/div[1]/section[1]/div/p")))
        descrption = descrption_element.text.strip()
    except Exception as e:
        descrption = None

    try:
        batch_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='flex flex-row items-center gap-[6px]']")))
        batch = batch_element.text.strip()
    except Exception as e:
        batch = None

    try:
        company_type_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Public')]")))
        company_type = company_type_element.text.strip()
    except Exception as e:
        company_type = None

    try:
        location_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, "//div[text()='San Francisco' and contains(@class, 'yc-tw-Pill')]")))
        location = location_element.text
    except Exception as e:
        location = None


    try:
        industry_tag_element1 = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[2]/section[1]/div[2]/div[1]/div[1]/div[2]/div[3]/a[2]/div")))
        industry_tag1 = industry_tag_element1.text.strip()
        industry_tags.append(industry_tag1)
    except Exception as e:
        pass

    try:
        industry_tag_element2 = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[2]/section[1]/div[2]/div[1]/div[1]/div[2]/div[3]/a[3]/div")))
        industry_tag2 = industry_tag_element2.text.strip()

        if industry_tag2 and industry_tag2 != location:
            industry_tags.append(industry_tag2)
    except Exception as e:
        pass
    try:
        website_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='group flex flex-row items-center px-3 leading-none text-linkColor ']/a")))
        website = website_element.text
    except Exception as e:
        pass

    try:
        founded_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='flex flex-row justify-between']/span[2]")))
        founded = founded_element.text
    except Exception as e:
        founded = None

    try:
        team_size_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
                                                                                           "//div[@class='flex flex-row justify-between']/span[1][text()='Team Size:']/following-sibling::span[1]")))
        team_size = team_size_element.text
    except Exception as e:
        team_size = None

    try:
        social_profiles1_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='space-x-2']/a[contains(@href, 'linkedin')]")))
        linkedin = social_profiles1_element.get_attribute("href")

    except Exception as e:
        linkedin = None

    try:
        social_profiles2_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='space-x-2']/a[contains(@href, 'twitter')]")))
        twitter = social_profiles2_element.get_attribute("href")

    except Exception as e:
        twitter = None

    try:
        social_profiles3_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='space-x-2']/a[contains(@href, 'facebook')]")))
        facebook = social_profiles3_element.get_attribute("href")

    except Exception as e:
        facebook = None

    try:
        social_profiles4_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='space-x-2']/a[contains(@href, 'crunchbase')]")))
        crunch_base = social_profiles4_element.get_attribute("href")

    except Exception as e:
        crunch_base = None

    try:
        social_profiles5_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='space-x-2']/a[contains(@href, 'github')]")))
        github = social_profiles5_element.get_attribute("href")

    except Exception as e:
        crunch_base = None
    # Founder 1
    try:
        founder1_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[2]/div/section/div[2]/div[1]/div[2]/div/div/div[1]")))
        founder1 = founder1_element.text.strip()
    except Exception as e:
        founder1 = None

    try:
        founder1_description_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/section/div[2]/div[1]/div[1]/p")))
        founder1_description = founder1_description_element.text.replace(founder1 + ' is the ', '')
    except Exception as e:
        founder1_description = None

    try:
        founder_social_profiles1_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div/div[2]/div/section/div[2]/div[1]/div[2]/div/div/div[2]/a[contains(@href, 'linkedin')]")))
        founder_linkedin = founder_social_profiles1_element.get_attribute("href")

    except Exception as e:
        founder_linkedin = None

    try:
        founder_social_profiles2_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div/div[2]/div/section/div[2]/div[1]/div[2]/div/div/div[2]/a[contains(@href, 'twitter')]")))
        founder_twitter = founder_social_profiles2_element.get_attribute("href")

    except Exception as e:
        founder_twitter = None

    # Founder2
    try:
        founder2_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[2]/div/section/div[2]/div[2]/div[2]/div/div/div[1]")))
        founder2 = founder2_element.text.strip()
    except Exception as e:
        founder2 = None
    try:
        founder2_description_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/section/div[2]/div[2]/div[1]/p")))
        founder2_description = founder2_description_element.text.replace(founder2 + ' is the ', '')
    except Exception as e:
        founder2_description = None

    try:
        founder2_social_profiles1_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
                                                                                                           "/html/body/div/div[2]/div/section/div[2]/div[2]/div[2]/div/div/div[2]//*[contains(@href, 'linkedin')]")))
        founder2_linkedin = founder2_social_profiles1_element.get_attribute("href")

    except Exception as e:
        founder2_linkedin = None

    try:
        founder2_social_profiles2_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
                                                                                                           "/html/body/div/div[2]/div/section/div[2]/div[2]/div[2]/div/div/div[2]//*[contains(@href, 'twitter')]")))
        founder2_twitter = founder2_social_profiles2_element.get_attribute("href")

    except Exception as e:
        founder2_twitter = None

    # Founder3
    try:
        founder3_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[2]/div/section/div[2]/div[3]/div[2]/div/div/div[1]")))
        founder3 = founder2_element.text.split(',')[0]
    except Exception as e:
        founder3 = None

    try:
        founder3_description_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/section/div[2]/div[3]/div[1]/p")))
        founder3_description = founder3_description_element.text.replace(founder3 + ' is the ', '')
    except Exception as e:
        founder3_description = None

    try:
        founder3_social_profiles1_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
                                                                                                           "/html/body/div/div[2]/div/section/div[2]/div[3]/div[2]/div/div/div[2]//*[contains(@href, 'linkedin')]")))
        founder3_linkedin = founder3_social_profiles1_element.get_attribute("href")

    except Exception as e:
        founder3_linkedin = None

    try:
        founder3_social_profiles2_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
                                                                                                           "/html/body/div/div[2]/div/section/div[2]/div[3]/div[2]/div/div/div[2]//*[contains(@href, 'twitter')]")))
        founder3_twitter = founder3_social_profiles2_element.get_attribute("href")

    except Exception as e:
        founder3_twitter = None

    # json file creation

    # Create the data
    company_info = {
        "Company": {
            "name": name,
            "tagline": tagline,
            "description": descrption,
            "batch": batch,
            "company_type": company_type,
            "industry_tags": industry_tags,
            "location": location,
            "website": website,
            "founded": founded,
            "team_size": team_size,
            "social_profiles": {
                "linkedin": linkedin,
                "twitter": twitter,
                "facebook": facebook,
                "crunchbase": crunch_base
            }
        },
        "founders": [
            {
                "name": founder1,
                "description": founder1_description,
                "twitter_profile": founder_twitter,
                "linkedin_profile": founder_linkedin
            },
            {
                "name": founder2,
                "description": founder2_description,
                "twitter_profile": founder2_twitter,
                "linkedin_profile": founder2_linkedin
            },
            {
                "name": founder3,
                "description": founder3_description,
                "twitter_profile": founder3_twitter,
                "linkedin_profile": founder3_linkedin
            }
        ]
    }

    driver.quit()

    # Return the extracted data
    return company_info

# Function to worker thread
def worker():
    index = 1  # Initialize index counter
    while True:
        url = queue.get()
        if url is None:
            break
        data = extract_data_from_website(url)
        with open('data.json', 'a') as json_file:
            json.dump(data, json_file, indent=4)
            json_file.write(',\n\n')
        print(f"Index: {index}, Data extraction completed for {url}")
        queue.task_done()
        index += 1


with open('Allcompany_links.txt', 'r') as file:
    urls = file.read().splitlines()


queue = Queue()

for url in urls:
    queue.put(url)


threads = []
for _ in range(10):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

queue.join()

# Stop workers
for _ in range(10):
    queue.put(None)

# Join threads
for t in threads:
    t.join()

print("All data extraction completed.")
