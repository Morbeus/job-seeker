import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from loguru import logger

load_dotenv()

class LinkedInAuth:
    def __init__(self):
        self.email = os.getenv('LINKEDIN_EMAIL')
        self.password = os.getenv('LINKEDIN_PASSWORD')
        self.driver = None
        
    def setup_driver(self):
        """Setup Chrome WebDriver with appropriate options"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
    def login(self):
        """Login to LinkedIn"""
        if not self.email or not self.password:
            raise ValueError("LinkedIn credentials not found in environment variables")
            
        try:
            self.setup_driver()
            self.driver.get('https://www.linkedin.com/login')
            
            # Enter email
            email_field = self.driver.find_element('id', 'username')
            email_field.send_keys(self.email)
            
            # Enter password
            password_field = self.driver.find_element('id', 'password')
            password_field.send_keys(self.password)
            
            # Click login button
            login_button = self.driver.find_element('xpath', '//button[@type="submit"]')
            login_button.click()
            
            logger.info("Successfully logged in to LinkedIn")
            return True
            
        except Exception as e:
            logger.error(f"Failed to login to LinkedIn: {str(e)}")
            return False
            
    def close(self):
        """Close the WebDriver"""
        if self.driver:
            self.driver.quit()
            self.driver = None 