from models.ticket_models import Ticket, Status
from models.job_model import Job_type
import datetime
from crudDB.ticket_CRUD import create_ticket

#name= input("Please insert your name ")
#request = Job_type(input("PLease insert job type "))


my_ticket = Ticket(id=1, user="JohnDoe", date_created=datetime.datetime.now(), type=Job_type.REQUEST, status=Status.PENDING)

create_ticket(my_ticket)
#new_ticket = Ticket(id=1, user = name, datetime = datetime.datetime.now(),status = Status.PENDING )





    