import json
import requests
import time
import os
import pprint

# API key is stored in config.json file
config = json.load(open("config.json"))
api_key = config["apiBingKey"]

endpoint = "https://api.bing.microsoft.com/"
url = f"{endpoint}v7.0/images/search"

new_offset = 0
headers = {"Ocp-Apim-Subscription-Key": api_key}

params = {
    "q": "snakes",
    "imageType": "photo"
}

contentUrls = []
response = requests.get(url, headers=headers, params=params)
response.raise_for_status()

result = response.json()

pprint.pprint(result)
while new_offset <= 5:
    # print(new_offset)
    params["offset"] = new_offset

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    result = response.json()

    time.sleep(1)

    new_offset = result["nextOffset"]

    for item in result["value"]:
        print(item["contentUrl"])
        contentUrls.append(item["contentUrl"])
dir_path = "./random_images/"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

