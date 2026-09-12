from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

routes = [
    {"id": 1, "from": "Chennai", "to": "Bangalore", "price": 800},
    {"id": 2, "from": "Chennai", "to": "Hyderabad", "price": 1200},
    {"id": 3, "from": "Chennai", "to": "Coimbatore", "price": 600},
    {"id": 4, "from": "Chennai", "to": "Pondicherry", "price": 400},
]

bookings = []

@app.route("/")
def home():
    return render_template("index.html", routes=routes)

@app.route("/book", methods=["POST"])
def book():
    data = request.get_json()
    name = data.get("name", "").strip()
    route_id = data.get("route_id")

    if not name or not route_id:
        return jsonify({"success": False, "message": "Please enter your name and select a route."}), 400

    route = next((r for r in routes if r["id"] == int(route_id)), None)
    if not route:
        return jsonify({"success": False, "message": "Invalid route."}), 400

    bookings.append({
        "name": name,
        "route": f'{route["from"]} → {route["to"]}',
        "price": route["price"]
    })
    return jsonify({"success": True, "message": f"Booking confirmed for {name}!"})

@app.route("/bookings")
def get_bookings():
    return jsonify(bookings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
