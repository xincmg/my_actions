

from helper import md5, output
from lxml import html

from sites.siteBase import SiteBase


class Oshwhub(SiteBase):
    def login(self) -> bool:
        url = 'https://passport.szlcsc.com/login'
        body = self._get_form_data()
        if not body:
            return False
        return self.post(url, data=body)

    def signin(self):
        response = self.get('https://oshwhub.com/sign_in')
        # output('.private\\login_result.html', response.text)
        dom = html.document_fromstring(response.text)
        self._threeday = dom.xpath(
            '//div[@id="home-content"]//div[@class="three-day"]/@data-status')[0]
        self._sevenday = dom.xpath(
            '//div[@id="home-content"]//div[@class="seven-day"]/@data-status')[0]
        headers = {
            'x-requested-with': 'XMLHttpRequest'
        }
        url = 'https://oshwhub.com/api/user/sign_in'
        response = self.post(url, headers=headers)
        return response

    def report(self, response):
        jsons = response.json()
        self.state = str(jsons)
        jsons = self._like().json()
        self.state += str(jsons)
        jsons = self._star().json()
        self.state += str(jsons)
        if jsons['result']['weekCount'] == 3 or self._threeday == '1':
            jsons = self._getTreeDayGift().json()
            self.state += str(jsons)
        if jsons['result']['weekCount'] == 7 or self._sevenday == '1':
            jsons = self._getSevenDayGift().json()
            self.state += str(jsons)

    def _like(self):
        headers = {
            'x-requested-with': 'XMLHttpRequest'
        }
        self.post(
            'https://oshwhub.com/api/projects/5089e537f97d4be1a13252fb120f9962/unlike', headers)
        return self.post('https://oshwhub.com/api/projects/5089e537f97d4be1a13252fb120f9962/like', headers)

    def _star(self):
        headers = {
            'x-requested-with': 'XMLHttpRequest'
        }
        self.post(
            'https://oshwhub.com/api/projects/5089e537f97d4be1a13252fb120f9962/unstar', headers)

        return self.post('https://oshwhub.com/api/projects/5089e537f97d4be1a13252fb120f9962/star', headers)

    def _getSevenDayGift(self):
        url = 'https://oshwhub.com/api/user/sign_in/getSevenDayGift'
        data = self._getUuidData()
        return self.post(url, data=data, headers={
            'x-requested-with': 'XMLHttpRequest'
        })

    def _getUuidData(self):
        url = 'https://oshwhub.com/api/user/sign_in/getUnbrokenGiftInfo'
        res = self.get(url, headers={
            'x-requested-with': 'XMLHttpRequest'
        }).json()
        return {
            'gift_uuid': res['result']['sevenDay']['uuid'],
            'coupon_uuid': res['result']['sevenDay']['coupon_uuid'],
        }

    def _getTreeDayGift(self):
        url = 'https://oshwhub.com/api/user/sign_in/getTreeDayGift'
        headers = {
            'x-requested-with': 'XMLHttpRequest'
        }
        return self.get(url, headers=headers)

    def _get_form_data(self) -> dict:
        url = 'https://passport.szlcsc.com/login'
        response = self.get(url)
        dom = html.document_fromstring(response.text)
        form = dom.get_element_by_id('fm1')
        body = []
        for field in form.inputs:
            if not field.name:
                continue
            # print(field.name, field.value)
            item = (field.name, field.value if field.value else '')
            body.append(item)
        body = dict(body)
        body['loginUrl'] = url
        body['username'] = self.user.name
        body['password'] = md5(self.user.token)
        del body['rememberPwd']
        # print('='*60)
        # print(json.dumps(body, indent=4))
        # print('='*60)
        if body['showCheckCodeVal'] == 'true':
            output('.private\\login_captcha.html', response.text)
            self.state = '请拖动滑块完成验证！'
        return body
