
import requests
from lxml import etree

from sites.siteBase import SiteBase


class Pthome(SiteBase):

    def login(self):
        self.session.headers.update({
            'Cookie': self.user.token,
        })

    def signin(self):
        url = 'https://www.pthome.net/attendance.php'
        try:
            response = self.session.get(url, timeout=5)
        except requests.RequestException as e:
            self.state = str(e)
            return None
        return response

    def report(self, response):
        if response.text.find('href="logout.php">退出</a>]')>=0:
            dom = etree.HTML(response.text)
            etree.strip_tags(dom, 'tbody', 'b', 'p')
            element = dom.xpath("//td[@class='embedded']/table/tr/td/text()")
            self.state = ''.join(element).strip()
        else:
            self.state = '未登录'

    def test(self):
        self.login()
        response = self.session.get(
            'https://www.pthome.net/index.php', timeout=5)
        print(response.text)
