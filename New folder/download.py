import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse

urlss=['https://www.reddit.com/r/memes/','https://www.reddit.com/r/wholesomememes/','https://www.reddit.com/r/dankmemes/','https://www.reddit.com/r/HistoryMemes/',]

def download_MEME():
    for subreddit_url in urlss:
        response = requests.get(subreddit_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        image_tags = soup.find_all('img')

        print(len(image_tags))
        # Create a directory to save the downloaded images
        if not os.path.exists('Meme'):
            os.makedirs('Meme')

        # Download images
        for img_tag in image_tags:
            img_url = img_tag.get('src')
            if img_url and 'jpg' in img_url.lower():
                img_data = requests.get(img_url).content
                img_filename = os.path.basename(urlparse(img_url).path)  # Extract filename from URL
                img_path = os.path.join('Meme', img_filename)
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Downloaded: {img_filename}")
        l=os.listdir('./Meme')
        if('X3dq7BwWSNeUHhYVAwg9EWZnzdW0rDaEwG8X76Th8PI.jpg' in l):
            os.remove("./Meme/X3dq7BwWSNeUHhYVAwg9EWZnzdW0rDaEwG8X76Th8PI.jpg")
