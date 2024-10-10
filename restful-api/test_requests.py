#!/usr/bin/python3
 
import requests
import csv

r = requests.get()

# Recover fetches all post from JSONPlaceholder and print status code
def fetch_and_print_posts():
    url = https://jsonplaceholder.typicode.com/posts

    response = requests.get(url)

    for post in posts:
        print(post["title"])

    if response.status_code == 200:
        posts = response.json()

        print("title of all the posts")

    else:
        print("failed to fetch posts")

def fetch_and_save_posts():