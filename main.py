from models.ticket_models import Ticket, Status
from models.job_model import Job_type
import datetime
from crudDB.ticket_CRUD import create_ticket

def select_type():
    for index, j in enumerate(Job_type,start=1):
        print(f"P{index}{j.value}")
    
    enum_type_size = len(Job_type)
    userCh = (input("select:\t"))
    while not userCh.isnumeric():
        userCh = (input("NUMBER :\t"))
    while int(userCh) > enum_type_size:
        userCh = (input("WRONG NUMBER:\t"))
    
    userCh = (int(userCh)-1)
    return return_JobType(userCh)
    
def str_to_int(x):
    return int(x)
    
def return_JobType(x):
    for index, i in enumerate(Job_type):
        if index == x:
            return i.value

    

NAME = input("PLease insert your name")
TYPE = select_type()


#test#my_ticket = Ticket(id=1, user="JohnDoe", date_created=datetime.datetime.now(), type=Job_type.REQUEST, status=Status.PENDING)
my_ticket = Ticket(id=None, user=NAME, date_created=datetime.datetime.now(), type=TYPE, status=Status.PENDING)


create_ticket(my_ticket)
#new_ticket = Ticket(id=1, user = name, datetime = datetime.datetime.now(),status = Status.PENDING )





    