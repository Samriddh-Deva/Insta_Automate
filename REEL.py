import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse

urls=['https://www.reddit.com/r/funnyvideos/']
# Specify the subreddit URL
for subreddit_url in urls:
# Send a GET request to the subreddit URL
    response = requests.get(subreddit_url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    # Find video posts
    video_posts = soup.find_all('div', {'class': 'scrollerItem'})

    # Create a directory to save the downloaded videos
    if not os.path.exists('downloaded_videos'):
        os.makedirs('downloaded_videos')

    # Download videos
    for post in video_posts:
        video_url = post.get('data-url')
        if video_url and video_url.endswith('.mp4'):  # Filter for MP4 videos
            # Extract filename from URL
            video_filename = os.path.basename(urlparse(video_url).path)
            video_path = os.path.join('downloaded_videos', video_filename)

            response = requests.get(video_url)
            if response.status_code == 200:
                with open(video_path, 'wb') as video_file:
                    video_file.write(response.content)
                    print(f"Downloaded: {video_filename}")
            else:
                print(f"Failed to download: {video_filename}")
