from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker

from dateutil.parser import parse


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

def scrape(postings):
    """
    Scrapes Craigslist and finds the latest listings.
    :return: A list of actually new results.
    """
    new_results = []

    for posts in postings:

        # For Debugging, print the craigslist ID
        #print result["id"]

        listing = session.query(Listing).filter_by(cl_id=posts["id"]).first()

        # Don't store the listing if it already exists.
        if listing is None:

            # Try parsing the price.
            price = 0
            try:
                price = float(posts["price"].replace("$", ""))
            except Exception:
                pass

            # Create the listing object.
            listing = Listing(
                link=posts["url"],
                created=parse(posts["datetime"]),
                name=posts["name"],
                price=price,    
                cl_id=posts["id"]
            )

            # Save the listing so we don't grab it again.
            session.add(listing)
            session.commit()
            new_results.append(result)

    return new_results

def do_scrape():
"""Runs the Craigslist scraper."""

    # Get all the results from craigslist.
    all_results = scrape(postings)

    print("{}: Got {} results".format(time.ctime(), len(all_results)))

    # Post each result to slack and email
    for result in all_results:
        pass