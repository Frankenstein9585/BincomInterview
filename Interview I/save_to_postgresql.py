import logging
from shirts import sorted_dict
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost/shirts_db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Shirts(Base):
    __tablename__ = 'shirts'

    id = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    color = Column(String, unique=True)
    frequency = Column(String)

    def __str__(self):
        return f'{self.color}: {self.frequency}'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for color, count in sorted_dict.items():
    new_shirt = Shirts(color=color, frequency=count)
    session.add(new_shirt)
    session.commit()


session.close()

