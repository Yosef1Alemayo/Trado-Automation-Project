import requests


class TestMenuPages:

    def test_clicking_snacks(self):
        # API url :
        url = "https://qa.trado.co.il/api/product/filter"
        # Copy the body :
        body = {
        "filter": {
        "sectionName": "חטיפים",
        "active": "true"
}}
        # Send POST request :
        response = requests.post(url, data=body)
        value = response.json()
        x = value['count']
        print(x)
        # verify the status code:
        assert response.status_code == 200
        assert x == 2

    def test_clicking_drinks(self):
        # API url :
        url = "https://qa.trado.co.il/api/product/filter"
        # Copy the body :
        body = {
            "filter": {
                "sectionName": "משקאות",
                "active": "true"
            }}
        # Send POST request :
        response = requests.post(url, data=body)
        value = response.json()
        x = value['count']
        print(x)
        print(value)
        # verify the status code:
        assert response.status_code == 200
        assert x == 0

    def test_clicking_sales(self):
        # API url :
        url = "https://qa.trado.co.il/api/product/filter"
        # Copy the body :
        body = {
            "filter": {
                "sectionName": "מבצעים",
                "active": "true"
            }}
        # Send POST request :
        response = requests.post(url, data=body)
        value = response.json()
        x = value['count']
        print(x)
        print(value)
        # verify the status code:
        assert response.status_code == 200
        assert x == 20


    def test_clicking_canabis(self):
        # API url :
        url = "https://qa.trado.co.il/api/product/filter"
        # Copy the body :
        body = {
            "filter": {
                "sectionName": "קנאביס",
                "active": "true"
            }}
        # Send POST request :
        response = requests.post(url, data=body)
        value = response.json()
        x = value['count']
        print(x)
        print(value)
        # verify the status code:
        assert response.status_code == 200
        assert x == 11