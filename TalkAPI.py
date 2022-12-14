import os
import requests
from dotenv import load_dotenv

load_dotenv()
DEFAULT_REQUEST_URL = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
API_KEY = os.environ.get('API_KEY')

def Talk_API(talk_context):
    data = {
        "apikey": API_KEY,
        "query": str(talk_context),
    }
    result = requests.post(DEFAULT_REQUEST_URL,data=data)
    return result

