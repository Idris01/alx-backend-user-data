#!/usr/bin/env python3
"""Flask app module
"""
from flask import Flask, jsonify, request
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound
from user import User


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Define the home route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """Handles user creation
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
        return jsonify(dict(email=email, message="user created"))
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
