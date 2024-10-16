#!/bin/python3


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return "welcome to the Flask API!"

if __name__ == "__main__":
    app.run(debug=True)