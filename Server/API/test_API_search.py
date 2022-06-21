import requests

class TestSearch():
     def test_valid_product(self):
         url = "https://qa.trado.co.il/api/user/update"
         mySearch = {"api_key": "1010101011rh", "id": "56586", "name": "אקדיה", "price":" 28.9", "catalog_num": "56586"}
         x = requests.post(url, json=mySearch )
         assert x.status_code == 200

     def test_invalid_product(self):
         url = "https://qa.trado.co.il/api/user/update"
         mySearch = {"uid": "1e1xpmlil4l4phx9", "lng": "hebrew", "platform": "web", "screenHeight": "864", "screenWidth": "1536"}
         x = requests.post(url, json=mySearch)
         assert x.status_code == 400