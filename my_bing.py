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

for url in contentUrls:
    split = url.split("/")

    last_item = split[-1]

    second_split = last_item.split("?")

    if len(second_split) > 1:
        last_item = second_split[0]

    third_split = last_item.split("!")

    if len(third_split) > 1:
        last_item = third_split[0]

    print(last_item)
    path = os.path.join(dir_path, last_item)

    try:
        with open(path, "wb") as f:
            image_data = requests.get(url)
            # image_data.raise_for_status()

            f.write(image_data.content)
    except OSError:
        pass