# LinkedIn Job Automation Tool

An automated tool to find and filter jobs from LinkedIn based on user preferences and requirements.

## Project Structure

```
job-seeker/
├── src/
│   ├── core/                    # Core functionality
│   │   ├── linkedin/           # LinkedIn specific operations
│   │   │   ├── scraper.py      # LinkedIn job scraping logic
│   │   │   ├── auth.py         # LinkedIn authentication
│   │   │   └── filters.py      # Job filtering logic
│   │   └── models/             # Data models
│   │       ├── job.py          # Job data structure
│   │       └── user.py         # User preferences
│   ├── utils/                  # Utility functions
│   │   ├── logger.py          # Logging configuration
│   │   └── helpers.py         # Helper functions
│   └── config/                 # Configuration files
│       └── settings.py         # Application settings
├── tests/                      # Test files
│   ├── core/
│   └── utils/
├── data/                       # Data storage
│   ├── jobs/                  # Scraped job data
│   └── logs/                  # Application logs
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables
```

## Features

- LinkedIn job scraping
- Advanced job filtering
- Customizable search criteria
- Data export capabilities
- Automated job application (optional)

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure `.env` file with LinkedIn credentials
4. Run the application

## Requirements

- Python 3.8+
- LinkedIn account
- Required Python packages (see requirements.txt)