#!/usr/bin/python3
 
import requests
import csv


# Recover fetches all post from JSONPlaceholder and print status code
def fetch_and_print_posts():
    url = https://jsonplaceholder.typicode.com/posts

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        print("title of all the posts")
        
    for post in posts:
        print(post["title"])

    else:
        print("failed to fetch posts")

def fetch_and_save_posts():