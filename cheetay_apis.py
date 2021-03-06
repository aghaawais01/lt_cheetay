from cheetay_base import CheetayBase
import json


class CheetayApis(CheetayBase):
    """
    User scripts for exercising the login
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(CheetayApis, self).__init__(*args, **kwargs)

    def login(self, user):
        """
        Authenticate the user.
        :param username: The user's username.
        :param password: The user's password.
        """
        url = self.hostname
        self.client.get(url, name='home_page')
        csrf = self.client.cookies['csrftoken']
        basketid = self.client.cookies['basket_id']
        sessionid = self.client.cookies['sessionid']

        post_url = self.hostname + "v3/oscarapi/login/"

        params = {
            "username": user,
            "password": "cheetay"
        }
        headers = {
            'Server': 'nginx/1.4.6 (Ubuntu)',
            'Date': 'Thu, 28 Oct 2019 09:32:18 GMT',
            'Content-Type': 'application/json',
            'Vary': 'Accept, Cookie',
            'Connection': 'keep-alive',
            'X-Frame-Options': 'SAMEORIGIN',
            'Allow': 'GET, POST, DELETE, HEAD, OPTIONS',
            'Set-Cookies': 'session_id={}; expires=Thu, 22-Oct-2020 09:32:18 GMT; Max-Age=31449600; Path=/'.format(
                sessionid),
            'Set-Cookies': 'csrftoken={}; expires=Thu, 05-Dec-2019 09:32:18 GMT; httponly; Max-Age=3628800; Path=/'.format(
                csrf),
            'Set-Cookies': 'basket_id={}; Path=/'.format(basketid)
        }
        response = self.client.post(post_url, data=json.dumps(params), headers=headers, name='login_session')
        return response

    def search_partner(self):
        post_url = self.hostname + 'v3/oscarapi/search/'

        params = {
            "area_id": 412,
            "city_id": 1,
            "area_name": "Thokar Niaz Beg",
            "page_size": 20,
            "page": 1,
            "food_query": "",
            "cuisines_filter": "",
            "sort_query": 1
        }

        headers = {
            'Server': 'nginx/1.4.6 (Ubuntu)',
            'Date': 'Thu, 28 Oct 2019 09:32:18 GMT',
            'Content-Type': 'application/json',
            'Referer': 'https://test.cheetay.pk/',
            'Vary': 'Accept, Cookie',
            'Connection': 'keep-alive',
            'X-Frame-Options': 'SAMEORIGIN',
            'Allow': 'GET, POST, DELETE, HEAD, OPTIONS',
            'X-CSRFToken': self.client.cookies['csrftoken'],
            'Set-Cookies': 'basket_id={}; Path=/'.format(self.client.cookies['basket_id'])
        }
        response = self.client.post(post_url, data=json.dumps(params), headers=headers, name='partner_search')
        self._check_response_data(response)

        return response

    def food_tiles(self):
        post_url = self.hostname + 'v3/oscarapi/food-tiles/?area_id=412'
        body = {
            "area": 412,
            "page": 1
        }
        headers = {
            'Server': 'nginx/1.4.6 (Ubuntu)',
            'Date': 'Thu, 28 Oct 2019 09:32:18 GMT',
            'Content-Type': 'application/json',
            'Referer': 'https://test.cheetay.pk/',
            'Vary': 'Accept, Cookie',
            'Connection': 'keep-alive',
            'X-Frame-Options': 'SAMEORIGIN',
            'Allow': 'GET, POST, DELETE, HEAD, OPTIONS',
            'X-CSRFToken': self.client.cookies['csrftoken'],
            'Set-Cookies': 'basket_id={}; Path=/'.format(self.client.cookies['basket_id'])
        }
        response = self.client.post(post_url, data=json.dumps(body), headers=headers, name='food_tiles')
        self._check_response_data(response)
        return response

    def restaurant_detail(self):
        get_url = self.hostname + 'v3/oscarapi/restaurants/karachi-kanteen?area_id=412'
        response = self.client.get(get_url)
        self._check_response_data(response)
        return response

    def add_basket(self):
        post_url = self.hostname + 'v3/oscarapi/basket/add-product/?multi_vender=true&area_id=412'
        body = {
            "url": "/oscarapi/products/181484/",
            "quantity": 1,
            "instructions": ""
        }
        headers = {
            'Server': 'nginx/1.4.6 (Ubuntu)',
            'Date': 'Thu, 28 Oct 2019 09:32:18 GMT',
            'Content-Type': 'application/json',
            'Referer': 'https://test.cheetay.pk/',
            'Vary': 'Accept, Cookie',
            'Connection': 'keep-alive',
            'X-Frame-Options': 'SAMEORIGIN',
            'Allow': 'GET, POST, DELETE, HEAD, OPTIONS',
            'X-CSRFToken': self.client.cookies['csrftoken'],
            'Set-Cookies': 'basket_id={}; Path=/'.format(self.client.cookies['basket_id'])
        }
        response = self.client.post(post_url, data=json.dumps(body), headers=headers, name='add_basket')
        self._check_response_data(response)
        return response