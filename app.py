from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

VALID_USERNAME = "admin"
VALID_PASSWORD = "Password123!"

@app.route("/")
def home():
    return "CST8919 Lab 2 - Flask Threat Detection App is running."

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        logging.info(f"LOGIN_SUCCESS username={username} ip={ip_address}")
        return jsonify({"message": "Login successful"}), 200
    else:
        logging.warning(f"LOGIN_FAILED username={username} ip={ip_address}")
        return jsonify({"message": "Invalid username or password"}), 401

if __name__ == "__main__":
    app.run()