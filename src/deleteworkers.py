import json
import requests
import os
import sys
import auth

filename = sys.argv[1]
with open(filename, "r") as file:
    all_workers = json.load(file)

session = requests.Session()
session.auth = (auth.USERNAME, auth.ACCESS_KEY)
for job in all_workers:
    res = session.delete(f"https://api.browserstack.com/5/worker/{job['id']}")
    n = os.write(sys.stdout.fileno(), res.content)
