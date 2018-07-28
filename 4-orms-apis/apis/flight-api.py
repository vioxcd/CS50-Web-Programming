# A particular API on Flight application


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """Return details about a single flight"""

    # Make sure flight exists
    if flight is None:
        return jsonify({"error": "invalid flight_id"}), 422

    # Get all passengers
    passengers = flight.passengers
    names = []
    for passenger in passengers:
        names.append(passenger.name)

    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passengers": names
    })
