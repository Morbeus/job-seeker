from typing import List
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..models.job import Job
from ..models.user import UserPreferences

class LinkedInScraper:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.linkedin.com/jobs/search/"
        
    def build_search_url(self, preferences: UserPreferences) -> str:
        """Build LinkedIn job search URL based on user preferences"""
        params = []
        
        # Add keywords
        if preferences.keywords:
            params.append(f"keywords={'%20'.join(preferences.keywords)}")
            
        # Add locations
        if preferences.locations:
            params.append(f"location={'%20'.join(preferences.locations)}")
            
        # Add experience levels
        if preferences.experience_levels:
            exp_levels = {
                'Internship': '1',
                'Entry level': '2',
                'Associate': '3',
                'Mid-Senior level': '4',
                'Director': '5',
                'Executive': '6'
            }
            exp_params = [exp_levels[level] for level in preferences.experience_levels if level in exp_levels]
            if exp_params:
                params.append(f"f_E={','.join(exp_params)}")
                
        # Add job types
        if preferences.job_types:
            job_types = {
                'Full-time': 'F',
                'Part-time': 'P',
                'Contract': 'C',
                'Temporary': 'T',
                'Volunteer': 'V',
                'Internship': 'I'
            }
            type_params = [job_types[job_type] for job_type in preferences.job_types if job_type in job_types]
            if type_params:
                params.append(f"f_JT={','.join(type_params)}")
                
        return f"{self.base_url}?{'&'.join(params)}"
        
    def scrape_jobs(self, preferences: UserPreferences) -> List[Job]:
        """Scrape jobs from LinkedIn based on user preferences"""
        try:
            url = self.build_search_url(preferences)
            self.driver.get(url)
            
            # Wait for job listings to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobs-search__results-list"))
            )
            
            jobs = []
            job_elements = self.driver.find_elements(By.CLASS_NAME, "job-card-container")
            
            for job_element in job_elements[:preferences.max_jobs]:
                try:
                    title = job_element.find_element(By.CLASS_NAME, "job-card-list__title").text
                    company = job_element.find_element(By.CLASS_NAME, "job-card-container__company-name").text
                    location = job_element.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
                    job_url = job_element.find_element(By.CLASS_NAME, "job-card-list__title").get_attribute("href")
                    
                    # Click on job to get description
                    job_element.click()
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "jobs-description"))
                    )
                    description = self.driver.find_element(By.CLASS_NAME, "jobs-description").text
                    
                    job = Job(
                        title=title,
                        company=company,
                        location=location,
                        description=description,
                        url=job_url
                    )
                    jobs.append(job)
                    
                except Exception as e:
                    logger.error(f"Error scraping job: {str(e)}")
                    continue
                    
            return jobs
            
        except Exception as e:
            logger.error(f"Error in job scraping: {str(e)}")
            return [] 