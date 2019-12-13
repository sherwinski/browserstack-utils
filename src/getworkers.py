import requests
import os
import sys
import auth
import time

session = requests.Session()
session.auth = (auth.USERNAME, auth.ACCESS_KEY)
res = session.get(f"https://api.browserstack.com/5/workers")
n = os.write(sys.stdout.fileno(), res.content)
print("\n")

filename = f"workers{time.time()}.json"
with open(filename, "w") as file:
    file.write(res.text)
    file.write("\n")

print(f"Created file {filename}")
