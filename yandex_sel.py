import os
import time
import requests
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

SEARCH_QUERY = "Coronella austriaca"
DOWNLOAD_FOLDER = "coronella_images"
IMAGES_TO_DOWNLOAD = 400

# Create download folder if it doesn't exist
Path(DOWNLOAD_FOLDER).mkdir(parents=True, exist_ok=True)


def download_images(query, download_folder, images_to_download):
    base_url = "https://yandex.com/images/search"
    url = base_url + "?text=" + query.replace(" ", "+")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    downloaded_images = 0
    last_scroll_height = driver.execute_script("return document.body.scrollHeight")

    

    driver.quit()


download_images(SEARCH_QUERY, DOWNLOAD_FOLDER, IMAGES_TO_DOWNLOAD)