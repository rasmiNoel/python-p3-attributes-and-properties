#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Noel", job="Admin"):
        self.name = name
        self.job = job
        
    @property
    def name(self):
        self._name_title=self._name.title()
        return self._name_title
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
