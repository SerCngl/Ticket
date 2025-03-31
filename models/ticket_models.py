#./models/ticket_models.py
from dataclasses import dataclass
import datetime
from models.job_model import JobType, Job_type
from enum import Enum

class Status(Enum):
    DENIED = "Denied"
    PROCESSED= "Processed"
    APPROVED= "Approved"
    PENDING= "Pending"
    


@dataclass
class Ticket:
    id: int
    user: str
    date_created: datetime
    type: Job_type
    status: Status
    