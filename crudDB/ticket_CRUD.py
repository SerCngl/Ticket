#./crudDB/ticket_CRUD.py

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.ticket_DB import Base, TicketDB
from models.ticket_models import Ticket

engine = create_engine("sqlite:///dataTicket.db")
Base.metadata.create_all(engine)

def create_ticket(x: Ticket):
    #try:
        new_Ticket = TicketDB(
            user= x.user,
            date_created = x.date_created,
            type = x.type,
            status = x.status
        )
        with Session(engine) as session:
            session.add(new_Ticket)
            session.commit()
            print(f"{x} has been created")
    #except:
    #    print("Error")
