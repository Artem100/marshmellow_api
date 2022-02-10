import requests

class RequesterCustom():

    def __init__(self, url: str, header=None):
        self.url = url
        self.headers = header

    def post_data(self, json_data):
        response = requests.post(self.url, headers=self.headers, json=json_data)
        return response
