import os
import re

files = os.listdir()
worker_name_pattern = re.compile(r"^workers(\w*).(\w*).json$")

for file in files:
    if re.match(worker_name_pattern, file):
        print("Deleting file: ", file)
        os.remove(file)
