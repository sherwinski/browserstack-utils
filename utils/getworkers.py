import requests
import os
import sys
from .auth import USERNAME, ACCESS_KEY
import time

def fetch_workers():
    session = requests.Session()
    session.auth = (USERNAME, ACCESS_KEY)
    res = session.get("https://api.browserstack.com/5/workers")
    n = os.write(sys.stdout.fileno(), res.content)
    print("\n")

    filename = f"workers{time.time()}.json"
    with open(filename, "w") as file:
        file.write(res.text)
        file.write("\n")

    print(f"Stored in new file {filename}")
