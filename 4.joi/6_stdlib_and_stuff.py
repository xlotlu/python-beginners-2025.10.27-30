# stdlib and stuff

# 1. os.path


from os import path
import os.path
from os import path as mypath

os.path is path is mypath


import ntpath
import posixpath

path is posixpath
path is ntpath

path.join("o-cale", "alta-cale", "ceva.txt")
path.join("/o-cale", "alta-cale", "ceva.txt")

path.dirname("/o/cale/lunga.txt")
path.split("/o/cale/lunga.txt")
dir, file = path.split("/o/cale/lunga.txt")
path.splitext("/o/cale/lunga.txt")
path.basename("/o/cale/lunga.txt")
path.splitext(path.basename("/o/cale/lunga.txt"))


# 2. alternativ: pathlib
import pathlib

p = pathlib.Path("/o/cale/lunga.txt")
p.absolute()

pathlib.Path("o/cale/lunga.txt").absolute()

p.parent


# 3. requests

# pip install requests
import requests

# some html
response = requests.get("https://example.org/")
print(response.text)
type(response.text)
response.content
response.headers
response.encoding

#some json
url = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(url)
data = response.json()
