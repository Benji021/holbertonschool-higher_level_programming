#!/bin/python3

import http.server

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return "welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "ok"

@app.route('/users/<usernames>')
def get_user(username):
    user = user.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "user not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({"error": "username is required"}), 400
    
    if username in users:
        return jsonify({"error": "user already exists"}), 400
    
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "user added", "user": users[username]})

if __name__ == "__main__":
    app.run(debug=True)
