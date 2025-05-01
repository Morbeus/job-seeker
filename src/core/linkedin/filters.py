from typing import List
from loguru import logger
from ..models.job import Job
from ..models.user import UserPreferences

class JobFilter:
    def __init__(self, preferences: UserPreferences):
        self.preferences = preferences
        
    def filter_jobs(self, jobs: List[Job]) -> List[Job]:
        """Filter jobs based on user preferences"""
        filtered_jobs = []
        
        for job in jobs:
            if self._matches_preferences(job):
                filtered_jobs.append(job)
                
        return filtered_jobs
        
    def _matches_preferences(self, job: Job) -> bool:
        """Check if a job matches user preferences"""
        try:
            # Check keywords
            if not self._contains_keywords(job):
                return False
                
            # Check exclude keywords
            if self._contains_exclude_keywords(job):
                return False
                
            # Check skills
            if not self._matches_skills(job):
                return False
                
            return True
            
        except Exception as e:
            logger.error(f"Error filtering job: {str(e)}")
            return False
            
    def _contains_keywords(self, job: Job) -> bool:
        """Check if job contains any of the keywords"""
        if not self.preferences.keywords:
            return True
            
        text = f"{job.title} {job.description} {job.company}".lower()
        return any(keyword.lower() in text for keyword in self.preferences.keywords)
        
    def _contains_exclude_keywords(self, job: Job) -> bool:
        """Check if job contains any exclude keywords"""
        if not self.preferences.exclude_keywords:
            return False
            
        text = f"{job.title} {job.description} {job.company}".lower()
        return any(keyword.lower() in text for keyword in self.preferences.exclude_keywords)
        
    def _matches_skills(self, job: Job) -> bool:
        """Check if job matches required skills"""
        if not self.preferences.skills:
            return True
            
        text = f"{job.description}".lower()
        return any(skill.lower() in text for skill in self.preferences.skills) 