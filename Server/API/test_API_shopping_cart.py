import requests


class TestShoppingCart:

    def test_adding_product_to_cart_correctly(self):
        url = "https://www.trado.co.il/api/analytics/addtoCart"
        body ={"eventData":{"api_key":"1010101011rh","prod_id":"56586","prod_name":"אקדיה","item_price":28.9,
                            "manufacturer_code":"","manufacturer_name":"","promotion_id":"","measure_units":"units",
                            "cookies":"cookies string","action_date":"2022-06-20T08:18:05.156Z","action":"add",
                            "num_items":1,"event_name":"add cart","store_id":"1010101011rh"}}
        # Send POST request :
        response = requests.post(url, data=body)
        print(response.json())
        # verify the status code:
        assert response.status_code == 200




