from dataclasses import dataclass
from typing import List, Optional

@dataclass
class UserPreferences:
    keywords: List[str]
    locations: List[str]
    experience_levels: List[str]
    job_types: List[str]
    salary_range: Optional[tuple[float, float]] = None
    skills: List[str] = None
    exclude_keywords: List[str] = None
    max_jobs: int = 100
    
    def __post_init__(self):
        if self.skills is None:
            self.skills = []
        if self.exclude_keywords is None:
            self.exclude_keywords = []
            
    def to_dict(self) -> dict:
        return {
            'keywords': self.keywords,
            'locations': self.locations,
            'experience_levels': self.experience_levels,
            'job_types': self.job_types,
            'salary_range': self.salary_range,
            'skills': self.skills,
            'exclude_keywords': self.exclude_keywords,
            'max_jobs': self.max_jobs
        } 