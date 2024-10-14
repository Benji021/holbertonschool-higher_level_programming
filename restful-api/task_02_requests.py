#!/usr/bin/python3
 
import requests
import json
import csv


# Recover fetches all post from JSONPlaceholder and print status code
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print("status_code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(post["title"])

    else:
        print("failed to fetch posts")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

    structured_data = [{
        "id": post["id"], "title": post["title"],
        "body": post["body"]} for post in posts]
    
    fieldnames = ["id", "title", "body"]

    with open("file.csv", mode="w", newline="") as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=fieldnames)

        writer.writeheader()

        for data in structured_data:
         writer.writerow(data)