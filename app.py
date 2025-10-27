from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
app = Flask(__name__)
CORS(app)
DATA_FILE = r"C:\ticket\data.json"
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
#Reserve Seats
@app.route("/reservations", methods=["POST"])
def reserve_seats():
    data = load_data()
    req = request.get_json()
    partner_id = req.get("partnerId")
    seats = req.get("seats") 
    if not partner_id or seats is None:
        return jsonify({"error"}), 400
    if seats <= 0 or seats > 10:
        return jsonify({"error"}), 400
    if data["availableSeats"] < seats:
        return jsonify({"error"}), 409
    reservation_id = f"res-{int(datetime.now().timestamp())}"
    data["availableSeats"] -= seats
    data["version"] += 1
    data["reservations"].append({
        "reservationId": reservation_id,
        "partnerId": partner_id,
        "seats": seats
    })
    save_data(data)
    return jsonify({
        "reservationId": reservation_id,
        "seats": seats,
        "status": "confirmed"
    }), 201
#Cancel Reservation
@app.route("/reservations/<reservation_id>", methods=["DELETE"])
def cancel_reservation(reservation_id):
    data = load_data()
    reservation_list = data["reservations"]
    found = next((r for r in reservation_list if r["reservationId"] == reservation_id), None)
    if not found:
        return jsonify({"error": "Reservation not found or already cancelled"}), 404
    data["availableSeats"] += found["seats"]
    data["reservations"].remove(found)
    data["version"] += 1
    save_data(data)
    return "", 204
#Get Event Summary
@app.route("/reservations", methods=["GET"])
def get_summary():
    data = load_data()
    summary = {
        "eventId": data["eventId"],
        "name": data["name"],
        "totalSeats": data["totalSeats"],
        "availableSeats": data["availableSeats"],
        "reservationCount": data["totalSeats"] - data["availableSeats"],
        "version": data["version"]
    }
    return jsonify(summary), 200
@app.route("/")
def home():
    return " TicketBoss Flask API is running"

if __name__ == "__main__":
    app.run(debug=True)