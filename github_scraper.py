import requests
import pandas as pd
import time

# GitHub API settings
GITHUB_TOKEN = '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'
headers = {'Authorization': f'token {GITHUB_TOKEN}'}
base_url = "https://api.github.com"

# 1. Fetch users in London with over 500 followers
def get_users(city="London", min_followers=500, max_results=100):
    users_data = []
    page = 1
    while len(users_data) < max_results:
        users_url = f"{base_url}/search/users?q=location:{city}+followers:>{min_followers}&page={page}&per_page=30"
        response = requests.get(users_url, headers=headers)
        response.raise_for_status()
        users = response.json().get('items', [])
        
        if not users:  # Stop if there are no more users
            break
            
        for user in users:
            users_data.append({
                "login": user['login'],
                "html_url": user['html_url'],  # GitHub profile link
            })
        
        page += 1
        time.sleep(1)  # Sleep to respect API rate limits
    
    return users_data

# Fetch users and print out the results
users = get_users()
print(f"Found {len(users)} users with over 500 followers in London.")
for user in users:
    print(user)
