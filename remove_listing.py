from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from dateutil.parser import parse

## Put Craigslist ID of the Craigslist item to delete here
cl_id_to_delete = 1234567890

engine = create_engine('sqlite:///listings.db', echo=False)
Base = declarative_base()

class Listing(Base):
    """
    A table to store data on craigslist listings.
    """

    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    name = Column(String)
    price = Column(Float)
    cl_id = Column(Integer, unique=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

rows = session.query(Listing).count()
print(f"{rows} rows in database")

listings = session.query(Listing).order_by(Listing.id.desc())

i = 0
for listing in listings:
    if( i > 15):
        break
    print(f"{listing.id}: {listing.name} - {listing.cl_id}")
    i+=1

session.query(Listing).filter_by(cl_id=cl_id_to_delete).delete()
session.commit()
print
print(f"Deleted: {cl_id_to_delete} ")

rows = session.query(Listing).count()
print(f"{rows} rows in database")