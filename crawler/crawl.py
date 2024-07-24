import requests
from bs4 import BeautifulSoup
from .models import SocialMediaPost

def crawl_social_media(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: Extract tweets from a Twitter page
        tweets = soup.find_all('div', class_='tweet')
        for tweet in tweets:
            content = tweet.find('p', class_='tweet-text').text
            SocialMediaPost.objects.create(content=content)
    else:
        print(f"Failed to retrieve content: {response.status_code}")
