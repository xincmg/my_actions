
import requests
from lxml import etree

from sites.siteBase import SiteBase


class Arduinocn(SiteBase):
    def login(self):
        self.session.headers.update({
            'Cookie': self.user.token,
        })

    def _get_formhash(self):
        url = 'https://www.arduino.cn/plugin.php?id=dsu_paulsign:sign'

        self.session.headers.update({
            # 'x-requested-with': 'XMLHttpRequest',
            'Referer': 'https://www.arduino.cn/plugin.php?id=dsu_paulsign:sign',
            'Host': 'www.arduino.cn',
            'Content-Type': 'application/x-www-form-urlencoded'
        })

        try:
            response = self.session.get(url, timeout=5)
        except requests.RequestException as e:
            self.state = str(e)
            return

        if '<p>您需要先登录才能继续本操作' in response.text:
            self.state = '您需要先登录才能继续本操作'
        elif '<h1 class="mt">您今天已经签到过了或者签到时间还未开始</h1>' in response.text:
            self.state = '您今天已经签到过了或者签到时间还未开始'
        else:
            dom = etree.HTML(response.text.encode())
            elements = dom.xpath('//form/input[@name="formhash"]')
            if len(elements):
                return elements[0].xpath('@value')[0]
            else:
                self.state = '找不到formhash'

    def signin(self):
        formhash = self._get_formhash()
        if not formhash:
            return

        url = 'https://www.arduino.cn/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1'
        obj = {
            'formhash': formhash,
            'qdxq': 'kx',
            'qdmode': '3',
            'todaysay': '',
            'fastreply': '0'
        }
        try:
            response = self.session.post(
                url=url,
                data=obj
            )
        except requests.RequestException as e:
            self.state = str(e)
            return
        return response

    def report(self, response):
        # 解析结果
        dom = etree.HTML(response.text)
        elements = dom.xpath('//body/div[@id="wp"]/div/div')
        if len(elements):
            text = elements[0].xpath('text()')[0].strip()
            self.state = text
