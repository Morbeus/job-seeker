from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Job:
    title: str
    company: str
    location: str
    description: str
    url: str
    posted_date: Optional[datetime] = None
    salary: Optional[str] = None
    experience_level: Optional[str] = None
    job_type: Optional[str] = None
    skills: list[str] = None
    
    def __post_init__(self):
        if self.skills is None:
            self.skills = []
            
    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'description': self.description,
            'url': self.url,
            'posted_date': self.posted_date.isoformat() if self.posted_date else None,
            'salary': self.salary,
            'experience_level': self.experience_level,
            'job_type': self.job_type,
            'skills': self.skills
        } 