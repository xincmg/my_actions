
import requests
from lxml import etree

from sites.siteBase import SiteBase


class Hdarea(SiteBase):

    def login(self):
        self.session.headers.update({
            'Cookie': self.user.token,
        })
        return True

    def signin(self):
        url = 'https://www.hdarea.co/sign_in.php'
        data = {'action' : 'sign_in'}
        try:
            response = self.session.post(url, data=data, timeout=5)
        except requests.RequestException as e:
            self.state = str(e)
            return None
        return response

    def report(self, response):        
        self.state = response.text
        print(self.state)
