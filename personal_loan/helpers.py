import requests
import json



def blacklist_status():

    url = "https://www.blacklistng.com/api/bvn/{}"

    payload={}
    headers = {
    'Authorization': 'kA8W2yijfSXpBUlpQezjI9qkmWZwi4Eq',
    'Accept': 'application/com.reloadly.topups-v1+json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)