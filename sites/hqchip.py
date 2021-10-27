import random
import time

from lxml import etree, html

from sites.siteBase import SiteBase


class Hqchip(SiteBase):

    def login(self) -> bool:
        headers = {
            'x-requested-with': 'XMLHttpRequest'
        }
        url = 'https://passport.elecfans.com/login/dologin.html?referer=https://www.hqchip.com'
        body={
            'referer': 'https://www.hqchip.com',
            'siteid': 12,
            'account': self.user.name,
            'password': self.user.token,
            'csessionid':'',
            'sig': '',
            'token': '',
            'aliscene': '',
        }
        response = self.post(url, data=body, headers=headers)
        json = response.json()
        if json['status'] == 'successed':
            for url in json['data']['syncurl']:
                if url.find('www.hqchip.com') > -1:
                    # 必要时判断返回值, if res.text=='failed' 登陆失败,无效token
                    self.get(url)
                    return True
        return False

    def signin(self):
        url = 'https://www.hqchip.com/exchange/signin'
        res = self.post(url, headers={
            'x-requested-with': 'XMLHttpRequest',
            'referer': 'https://www.hqchip.com/exchange.html'
        })
        return res

    def report(self, response):
        json = response.json()
        self.state = str(json)
