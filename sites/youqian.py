import json
import time

import requests
from requests.adapters import Response

from sites.siteBase import SiteBase


class Youqian(SiteBase):

    def __init__(self, flag, user):
        super().__init__(flag, user)
        self._result = []

    def login(self):
        self.session.headers.update({
            'Cookie': self.user.token,
        })

    def signin1(self):
        '''360有钱签到'''
        self.session.headers.update({
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://youqian.360.cn/score.html',
        })
        ts = int(time.time() * 1000)
        url = f'http://youqian.360.cn/sign/sign?t={ts}'
        try:
            response = self.session.get(url, timeout=5)
        except requests.RequestException as e:
            self.state = str(e)
            return None
        return response

    def signin2(self):
        '''安全盾签到'''
        self.session.headers.update({
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://youqian.360.cn/task.html',
        })
        ts = int(time.time() * 1000)
        url = f'http://youqian.360.cn/task/finishtask?type=1&t={ts}'
        try:
            response = self.session.get(url, timeout=5)
        except requests.RequestException as e:
            self.state = str(e)
            return None
        return response

    def report(self, response: Response):
        jsons = response.json()
        self._result.append(json.dumps(jsons)+'\n')

    def run(self):
        self.login()
        response = self.signin1()
        if response is None:
            return
        self.report(response)

        response = self.signin2()
        if response is None:
            return
        self.report(response)

    @property
    def result(self):
        return f'{self.flag}：{self.user.name}\n{"".join(self._result)}'
