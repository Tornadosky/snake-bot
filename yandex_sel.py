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

    while downloaded_images < images_to_download:
        # Scroll down to load more images
        ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(2)

        # Check if the scroll height has changed
        new_scroll_height = driver.execute_script("return document.body.scrollHeight")
        if new_scroll_height == last_scroll_height:
            break
        last_scroll_height = new_scroll_height

        images = driver.find_elements(By.CSS_SELECTOR, "img.serp-item__thumb")

        for img in images:
            if downloaded_images >= images_to_download:
                break

            img_url = img.get_attribute("src")
            if not img_url:
                img_url = img.get_attribute("data-src")

            if not img_url:
                continue

            try:
                img_data = requests.get(img_url).content
                with open(os.path.join(download_folder, f"{downloaded_images}_grasse.jpg"), "wb") as f:
                    f.write(img_data)
                downloaded_images += 1
                print(f"Downloaded image {downloaded_images}: {img_url}")
            except Exception as e:
                print(f"Failed to download {img_url}: {e}")

    driver.quit()


download_images(SEARCH_QUERY, DOWNLOAD_FOLDER, IMAGES_TO_DOWNLOAD)