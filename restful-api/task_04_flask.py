#!/usr/bin/env python3


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "jane", "age": 28, "city": "Los Angeles"}
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
