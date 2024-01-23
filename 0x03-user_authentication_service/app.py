#!/usr/bin/env python3
"""Flask app module
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Define the home route
    """
    return jsonify(dict(message="I am a Software Engineer"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
