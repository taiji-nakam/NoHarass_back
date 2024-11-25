from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
 

class Base(DeclarativeBase):
    pass


class Customers(Base):
    __tablename__ = 'customers'
    customer_id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_name:Mapped[str] = mapped_column()
    age:Mapped[int] = mapped_column()
    gender:Mapped[str] = mapped_column()
    