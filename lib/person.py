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
    def __init__(self, name, job):
        self.name = name.upper()
        self.job = job
    
    def save_name(self, name):
        if (type(name) in (name, str)) and len(name) > 0 and len(name) < 25:
            self.name = name
        
        else:
            print("Name must be string under 25 characters.")

    name = property(save_name)
    
    def save_job(self, job):
        if (type(job) in (job, str)) and job in APPROVED_JOBS:
            self.job = job
        
        else:
            print("Job must be in list of approved jobs.")
            
    job = property(save_job)
