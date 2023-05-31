import requests
# python -m venv env
# call env/scripts/activate
# pip install requests

url = "https://jsonplaceholder.typicode.com/posts/66"
data = requests.get(url)
print(type(data.json()))
print(data.json())
