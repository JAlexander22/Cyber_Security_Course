import requests

request_bbc = requests.get("https://www.bbc.com")
print("==================================The Status Code==============")
print(request_bbc.status_code)
input()
print("==================================The Content==============")
print(request_bbc.content)