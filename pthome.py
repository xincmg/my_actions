import os

from lxml import etree
import requests


def main():
    cookie = os.environ["COOKIE"]
    url = 'https://www.pthome.net/attendance.php'
    headers = {
        'Cookie': cookie,
        'Host': 'www.pthome.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    }
    response = requests.get(url, headers=headers)

    if response.text.find('<h1>未登录!</h1>') == -1:
        dom = etree.HTML(response.text)
        etree.strip_tags(dom, 'tbody', 'b', 'p')
        element = dom.xpath("//td[@class='embedded']/table/tr/td/text()")
        result = ''.join(element).strip()
    else:
        result = '未登录'
    print('pthome签到：' + result)
    print('\n')


if __name__ == "__main__":
    # 'Cookie': 'c_secure_uid=MTE2NTg0; c_secure_pass=f99543af6063c1fad5110dbf5c73e874; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; __cfduid=dea69407abd185e7cc8234df543a770cf1599732509',
    main()
