# In python we have various built in modules
# We can use external modules created by someone else as well

import requests as req
import json

# https://newsapi.org | Web Service
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=31c21508fad64116acd229c10ac11e84"

# Sending a Request to News API Server which sends back a Response which will be JSON
# HTTP Operation
response = req.get(url)
# req.post(url, pass data here)

print(response.text) # JSON Response
print(type(response))

print()

# We are converting JSON into Python Dictionary
news = json.loads(response.text)
print(news)
print(type(news))

print()

print("Total Results:",news["totalResults"])
print("===Article at 0th Index===")
print(news["articles"][0])
print(news["articles"][0]["author"])
print(news["articles"][0]["title"])

print("==========================")

total = news["totalResults"]
for i in range(0, total):
    print(news["articles"][i]["author"])
    print(news["articles"][i]["title"])
    print("=====================")



