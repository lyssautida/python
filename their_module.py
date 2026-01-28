# pip install requests pypi.org
import requests

url = "https://www.example.com"
response = requests.get(url) 
print(f"HTTP Request '{url}' returned status {response.status_code}") 