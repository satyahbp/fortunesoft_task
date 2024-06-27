from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class OfficesModel(Base):
    __tablename__ = "offices"

    officeCode = Column(String(10), primary_key=True, nullable=False)
    city = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False) 
    addressLine1 = Column(String(50), nullable=False)
    addressLine2 = Column(String(50), default=None, nullable=True)
    state = Column(String(50), default=None, nullable=True)
    country = Column(String(50), nullable=False)
    postalCode = Column(String(15), nullable=False)
    territory = Column(String(10), nullable=False)


class EmployeesModel(Base):
    __tablename__ = "employees"

    employeeNumber = Column(Integer, primary_key=True, nullable=False)
    lastName = Column(String(50), nullable=False)
    firstName = Column(String(50), nullable=False)
    extension = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    officeCode = Column(String(10), nullable=False)
    reportsTo = Column(Integer, default=None, nullable=True)
    jobTitle = Column(String(50), nullable=False)

