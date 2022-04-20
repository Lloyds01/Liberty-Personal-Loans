import requests
from django.conf import settings



class ExternalCheck:

    def __init__(self):

        self.blacklist_base_url = "https://www.blacklistng.com/api/bvn/"

        self.crc_base_url = "https://blacklistng.com/api/crc-bvn-search/"

        self.api_key = settings.BLACKLIST_API_KEY

    def blacklist_status(self, bvn):

        url = f"{self.blacklist_base_url}/{bvn}"

        headers = {
        'Authorization': self.api_key,
        'Accept': 'application/com.reloadly.topups-v1+json'
        }

        response = requests.request("GET", url, headers=headers)

        try:
            return response.json()
        except:
            return False

    def crc_status(self, bvn):

        url = f"{self.crc_base_url}/{bvn}"

        headers = {
        'Authorization': self.api_key,
        'Accept': 'application/com.reloadly.topups-v1+json'
        }

        response = requests.request("GET", url, headers=headers)

        try:
            return response.json()
        except:
            return False
