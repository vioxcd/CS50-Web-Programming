# SQL syntax are changed into ORMs

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    # BEFORE
    """
    flights = db.execute("SELECT * FROM flights").fetchall()
    """
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists
    # BEFORE
    """
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flights with that id.")
    """
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flights with that id.")

    # Add Passenger
    # BEFORE
    """
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
               {"name": name, "flight_id": flight_id})

    db.commit()
    return render_template("success.html")
    """

    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template("success.html")


@app.route("/flights")
def flights():
    """List all flights."""
    # BEFORE
    """
    flights = db.execute("SELECT * FROM flights").fetchall()
    """

    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists
    # BEFORE
    """
    flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
    """
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flights")

    # Get all passengers
    # BEFORE
    """
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    """
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template("fligh.thtml", passengers=passengers)


if __name__ == "__main__":
    app.run()
