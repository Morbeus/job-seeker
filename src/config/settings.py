import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LinkedIn Configuration
LINKEDIN_EMAIL = os.getenv('LINKEDIN_EMAIL')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

# Application Settings
MAX_JOBS_PER_SEARCH = 100
REQUEST_TIMEOUT = 30
SLEEP_BETWEEN_REQUESTS = 2

# Data Storage
JOBS_DATA_DIR = "data/jobs"
LOGS_DIR = "data/logs"

# Create necessary directories
os.makedirs(JOBS_DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True) 