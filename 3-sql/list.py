import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    # fetchall returns list datatype
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes")

if __name__ == "__main__":
    main()
