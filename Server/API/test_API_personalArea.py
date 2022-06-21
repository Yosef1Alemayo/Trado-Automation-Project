import requests

class TestRegisterArea():
    def test_valid_area(self):
        url = "https://qa.trado.co.il/api/user/update"
        myRegister = {"firstName": "Jonathan", "lastName": "Elias", "phone": "0522578853", "email": "gonathan46@gmail.com","city":"" , "street": "" ,"building": "5"}
        x = requests.post(url,json=myRegister)
        assert x.status_code == 200

    def test_invalid_area(self):
        url = "https://qa.trado.co.il/api/user/update"
        myRegister = {"firstName": "Jon", "lastName": "wik", "phone": "0522578853","email": "gonathan46@gmail.com", "city": "", "street": "", "building": "5"}
        x = requests.post(url, json=myRegister)
        assert x.status_code == 400


