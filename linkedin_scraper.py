from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_linkedin_jobs(job_title, location):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Set up the driver (make sure chromedriver is in your PATH)
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to LinkedIn jobs search page
    linkedin_url = "https://www.linkedin.com/jobs/search/"
    driver.get(linkedin_url)
    time.sleep(2)  # Wait for the page to load
    try:
        driver.find_element(By.CLASS_NAME,'contextual-sign-in-modal__modal-dismiss-icon').click()
    except:
        print('login dismiss not found')
        
    # Input the job title
    search_title_box = driver.find_element(By.XPATH, '//input[@aria-label="Search job titles or companies"]')
    search_title_box.send_keys(job_title)
    
    # Input the location
    search_location_box = driver.find_element(By.XPATH, '//input[@aria-label="Location"]')
    search_location_box.clear()  # Clear the default location
    search_location_box.send_keys(location)
    
    # Click the search button
    search_button = driver.find_element(By.CSS_SELECTOR, '#jobs-search-panel > form > button > icon > svg')
    search_button.click()

    
    time.sleep(3)  # Wait for search results to load

    # Scrape the job listings
    job_listings = []
    job_elements = driver.find_elements(By.CLASS_NAME, 'jobs-search__results-list')
    job_elements = job_elements[0].find_elements(By.TAG_NAME,'li')

    for job_element in job_elements:
        try:
            job_title = job_element.find_element(By.CLASS_NAME, 'base-search-card__info').text
            company_name = job_element.find_element(By.CLASS_NAME, 'base-search-card__subtitle').text
            location = job_element.find_element(By.CLASS_NAME, 'job-search-card__location').text
            job_link = job_element.find_element(By.TAG_NAME, 'a').get_attribute('href')

            job_listings.append({
                'Job Title': job_title,
                'Company': company_name,
                'Location': location,
                'Link': job_link
            })
        except Exception as e:
            print(f"Error while scraping job: {e}")
            continue
    
    # Close the driver
    driver.quit()

    return job_listings



if __name__ == "__main__":
    job_title = "Data Engineer"
    location = "Montreal, Quebec, Canada"
    
    jobs = scrape_linkedin_jobs(job_title, location)
    
    for i, job in enumerate(jobs, start=1):
        print(f"Job {i}:")
        print(f"Title: {job['Job Title']}")
        print(f"Company: {job['Company']}")
        print(f"Location: {job['Location']}")
        print(f"Link: {job['Link']}")
        print("-" * 20)
