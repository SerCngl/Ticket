#./models/job_model.py
from dataclasses import dataclass
from enum import Enum

class Job_type(Enum):
    REQUEST = "request"
    INCIDENT = "incident"
    SERVICE = "service"
    ACCESS =  "access"
    

@dataclass
class JobType:
    id: int
    job_type: Job_type