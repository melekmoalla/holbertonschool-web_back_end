#!/usr/bin/env python3
"""
Flask application to return a welcome message.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methode=["GET"])
def welcome():
    """Return a welcome message."""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
