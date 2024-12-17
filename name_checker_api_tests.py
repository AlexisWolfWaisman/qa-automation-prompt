import requests
from faker import Faker
import random
import Database_handler
import time
import string
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
        def search_pattern(name):
            for myVar in range(2):
                status_code, response = self.check_name(name)
                if status_code == 200 :
                        print(f"Name: {name} is a valid name")
                        break
                resp = response["message"]                             
                if status_code == 500 and resp != "System is down":
                    print(f" {name} - Response: {response}")
                    return True        
        def generate_random_name():
        
            chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:'\"<>,.?/" + "áéíóú😊🚀测试"
            length = random.choice(range(1, 256))  # Longitud aleatoria entre 1 y 255
            return ''.join(random.choices(chars, k=length))
        #trying with names from different countries        
        faker_country_codes = [
    "ar_AE", "ar_PS", "ar_SA", "bg_BG", "cs_CZ", "de_AT", "de_CH", "de_DE",
    "dk_DK", "el_GR", "en_AU", "en_CA", "en_GB", "en_IE", "en_IN", "en_NZ",
    "en_PH", "en_US", "es_AR", "es_CL", "es_CO", "es_ES", "es_MX","et_EE", 
    "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_CH", "fr_FR", "he_IL",
    "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_IT", "ja_JP", "ka_GE",
    "ko_KR", "lt_LT", "lv_LV", "ne_NP", "nl_BE", "nl_NL", "no_NO", "pl_PL",
    "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sq_AL", 
    "sv_SE"]
        for country_code in faker_country_codes:
            fake = Faker(country_code)
            names = [fake.first_name() for _ in range(2)]
            for name in names:
                flag = search_pattern(name)
                if flag:
                    break       
        # trying with some known patterns
        possibleNames = ["", "@#$$%", "1234", "Jhon","jHoN","Jhon123","Jhon Simpson", " ","18.28","jhon.simpson@xmail.com", "www.jhonsimpson.com" ]
        for name in possibleNames:
            flag = search_pattern(name)
            if flag:
                break
   
        
      #if everything above fails, we will try with random names
        while True: 
            name = generate_random_name()   
            flag = search_pattern(name)
            if flag:
                break                  

    def populate_database(self,maxTime=5):
        fake = Faker()
        names = [fake.first_name() for _ in range(1000)]
        i = 0
        db_conn = Database_handler.Db_connection()
        start_time = time.time()
        while time.time() - start_time < maxTime: 
            name = names[i]            
            status_code, response = self.check_name(name)
            record = (self.get_url(), name, status_code, list(response.keys())[0])
            db_conn.insert_record(self.get_url(), name, status_code, list(response.keys())[0])
            i += 1
        db_conn.close()


