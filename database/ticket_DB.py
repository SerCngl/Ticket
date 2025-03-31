#./database/ticket_DB.py

from sqlalchemy import Numeric, String, Date, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from models.job_model import JobType
from models.ticket_models import Ticket, Status, Job_type


class Base(DeclarativeBase):
    pass

class TicketDB(Base):
    __tablename__ = "ticket"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    user: Mapped[str] = mapped_column(String(64))
    date_created: Mapped[Date] = mapped_column(Date)
    type: Mapped[JobType] = mapped_column(Enum(Job_type))
    status: Mapped[Status] = mapped_column(Enum(Status))
    