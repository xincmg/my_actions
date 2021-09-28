import requests
from lxml import etree

from sites.siteBase import SiteBase


class Elecfans(SiteBase):

    def login(self):
        self.session.headers.update({
            'Cookie': self.user.token,
        })

    def _get_formhash(self):
        self.session.headers.update({
            'Referer': 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign',
            'x-requested-with': 'XMLHttpRequest',
            'Host': 'bbs.elecfans.com',
        })
        url = f'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign&{self.user.name}&infloat=yes&handlekey=dsu_paulsign&inajax=1&ajaxtarget=fwin_content_dsu_paulsign'
        try:
            response = self.session.get(url, timeout=5)
        except requests.RequestException as e:
            self.state = str(e)
            return None

        # formhash = ''
        if response.text.find('<h1>未登录!</h1>') >= 0:
            self.state = '未登录'
        elif response.text.find('<h1 class="mt">您今天已经签到过了或者签到时间还未开始</h1>') >= 0:
            self.state = '您今天已经签到过了或者签到时间还未开始'
        else:
            dom = etree.HTML(response.text.encode())
            elements = dom.xpath('//form/div/input[@name="formhash"]')
            if len(elements):
                return elements[0].xpath('@value')[0]
        # return formhash

    def signin(self):
        formhash = self._get_formhash()
        if not formhash:
            return
        # post data

        url = 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1'
        obj = {
            'formhash': formhash,
            'qdxq': 'kx',
            'qdmode': '3',
            'todaysay': '',
            'fastreply': '0'
        }
        # self.session.headers.update({'content-type':'application/x-www-form-urlencoded'})
        headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        try:
            response = self.session.post(
                url=url,
                data=obj,
                headers=headers,
            )
        except requests.RequestException as e:
            self.state = str(e)
            return

        return response

    def report(self, response):
        # 解析结果
        dom = etree.HTML(response.text.replace('\r\n', ''))
        elements = dom.xpath('//body/div[@id="wp"]/div/div/div')
        if len(elements):
            text = elements[0].xpath('string(.)')
            self.state = text  # 保存签到结果
