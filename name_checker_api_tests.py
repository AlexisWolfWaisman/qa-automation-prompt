import requests
from faker import Faker
import random

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
    
    def diagnose_system_errors(self):
        fake = Faker() 
        rand = random.Random()
        abc = "abcdefghijklmnopqrstuvwxyz"
        testNames = ("123","1.5", "True", "!%&", "!%jhon###&//martin" , "Jhon", "JHON", "Jhon123","jHoN","","Jh0n", "7jhon", "jh0n" ,  "Jhon Martin",
            "jhon martin", "jhon.martin@mymail.com", "perepia","https://es.wikipedia.org/wiki", "+2064223358")
        def search_pattern(name):
            for myVar in range(3):
                status_code, response = self.check_name(name)
                if status_code == 200 :
                        print(f"Name: {name} is a valid name")
                        break
                resp = response["message"]                             
                if resp == "System is down":                    
                    print(f"{name} - shuts down the system ")
                else:
                    print(f" {name} matched with pattern")
                    print(f"Response: {response} - Status code: {status_code}") 
        for letter in abc:
            name = letter  
            search_pattern(name)        
        for letter in abc:
            group = abc.replace(letter,"")
            name = letter + group[rand.randint(0,24)]
            name = name + name[::-1]            
            search_pattern(name)
        for name in testNames:
            search_pattern(name)
        for i in range(10):
                    name = fake.first_name()                
                    search_pattern(name) 
                       

