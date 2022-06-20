import requests


class TestShoppingCart:

    def test_adding_product_to_cart_correctly(self):
        # API url :
        url = "https://www.trado.co.il/api/analytics/addtoCart"
        # Copy the body :
        body = ''
        # Send POST request :
        response = requests.post(url, data=body)
        print(response.json())
        # verify the status code:
        assert response.status_code == 200