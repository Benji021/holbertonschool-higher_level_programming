#!/usr/bin/env python3


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

#Home route
@app.route('/')
def home():
    return "welcome to the Flask API!"

#Data route
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

#Status route
@app.route('/status')
def status():
    return "OK"

#Specific User by Username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "user not found"}), 404

#add new User
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if username and username not in users and name and isinstance(age, int) and city:
            users[username] = {
                "name": name,
                "age": age,
                "city": city
            }
            return jsonify(
                {"message": "User added", "user": users[username]}), 201
    else:
        return jsonify(
            {"error": "Invalid data or user already exists"}), 400

if __name__ == "__main__":
    app.run(debug=True)
