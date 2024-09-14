from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class JobScraper:
    def __init__(self, headless=True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=chrome_options)

    def navigate_to_linkedin(self):
        linkedin_url = "https://www.linkedin.com/jobs/search/"
        self.driver.get(linkedin_url)
        time.sleep(2)

    def input_search_details(self, job_title, location):
        try:
            self.driver.find_element(By.CLASS_NAME, 'contextual-sign-in-modal__modal-dismiss-icon').click()
        except:
            print('Login dismiss not found')

        search_title_box = self.driver.find_element(By.XPATH, '//input[@aria-label="Search job titles or companies"]')
        search_title_box.send_keys(job_title)

        search_location_box = self.driver.find_element(By.XPATH, '//input[@aria-label="Location"]')
        search_location_box.clear()
        search_location_box.send_keys(location)

        search_button = self.driver.find_element(By.CSS_SELECTOR, '#jobs-search-panel > form > button > icon > svg')
        search_button.click()
        time.sleep(1)

    def scrape_jobs(self):
        job_listings = []
        for i in range(8):
            self.scroll_to_end()

        job_elements = self.driver.find_elements(By.CLASS_NAME, 'jobs-search__results-list')[0].find_elements(By.TAG_NAME, 'li')

        for job_element in job_elements:
            job_info = self.extract_job_info(job_element)
            if job_info:
                job_listings.append(job_info)

        return job_listings

    def extract_job_info(self, job_element):
        try:
            job_title = job_element.find_element(By.CLASS_NAME, 'base-search-card__info').text
            company_name = job_element.find_element(By.CLASS_NAME, 'base-search-card__subtitle').text
            location = job_element.find_element(By.CLASS_NAME, 'job-search-card__location').text
            job_link = job_element.find_element(By.TAG_NAME, 'a').get_attribute('href')

            description = self.get_job_description(job_element)
            return {
                'Job Title': job_title,
                'Company': company_name,
                'Location': location,
                'Link': job_link,
                'Description': description
            }
        except Exception as e:
            print(f"Error extracting job info: {e}")
            return None

    def get_job_description(self, job_element):
        for retry in range(3):
            try:
                link = job_element.find_element(By.CLASS_NAME, 'base-card__full-link')
                link.click()
                time.sleep(3)
                return self.driver.find_element(By.CLASS_NAME, 'show-more-less-html__markup').text
            except Exception as e:
                print(f"Failed to get description: {e}")
                time.sleep(2)
        return '-'

    def scroll_to_end(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def close(self):
        self.driver.quit()
