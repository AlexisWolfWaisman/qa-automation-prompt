import requests

class NameCheckerAPI:
    def __init__(self):
        self.__url: str = ""
        self.__headers: dict = {} 
        self.__payload: dict = {}
    
    def set_payload(self, name):
        self.__payload["name"] = name

    def get_payload(self):
        return self.__payload
    
    def set_url(self, url):
        self.__url = url

    def get_url(self):
        return self.__url

    def set_headers(self, headers):
        self.__headers = headers

    def get_headers(self):
        return self.__headers
    
    def check_name(self, p_name):
        self.set_url("https://qa-challenge-nine.vercel.app/api/name-checker")
        self.set_headers({"Content-Type": "application/json"})
        self.set_payload({"name": p_name})
        response = requests.post(self.get_url(), headers=self.get_headers(), json=self.get_payload())
        return response.status_code, response.json()