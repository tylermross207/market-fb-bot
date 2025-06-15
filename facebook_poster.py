import requests
import os
from dotenv import load_dotenv

load_dotenv()

def post_to_facebook(message):
    page_access_token = os.getenv('PAGE_ACCESS_TOKEN')
    page_id = os.getenv('PAGE_ID')
    url = f'https://graph.facebook.com/{page_id}/feed'
    payload = {
        'message': message,
        'access_token': page_access_token
    }
    response = requests.post(url, data=payload)
    return response.json()
