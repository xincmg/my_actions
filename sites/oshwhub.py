import requests
from sites.siteBase import SiteBase


class Oshwhub(SiteBase):
    def login(self):
        self.session.headers.update({
            'Cookie': self.user.token,
        })

    def signin(self):
        self.session.headers.update({
            'referer': 'https://oshwhub.com/sign_in',
            'x-requested-with': 'XMLHttpRequest'
        })
        url = 'https://oshwhub.com/api/user/sign_in'
        try:
            response = self.session.post(url, timeout=5)
        except requests.RequestException as e:
            self.state = str(e)
            return None
        return response

    def report(self, response):
        jsons = response.json()
        self.state = str(jsons)
