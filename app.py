
from flask import Flask, jsonify, request

app = Flask(__name__)
events = []

@app.post("/event")
def add_event():
    data = request.json
    events.append(data)
    return {"status":"ok"}

@app.get("/events")
def get_events():
    return jsonify(events)

if __name__ == "__main__":
    app.run()
