import os
from lxml import etree
import requests

uid='4726590'
# uid = '4757904'
cookie = os.environ["COOKIE"]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',    
    'x-requested-with': 'XMLHttpRequest',
    'Referer': 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign',
    'Host': 'bbs.elecfans.com',
    'Cookie': cookie,
}
_session = requests.Session()


def main():
    # get formhash    
    url = f'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign&{uid}&infloat=yes&handlekey=dsu_paulsign&inajax=1&ajaxtarget=fwin_content_dsu_paulsign'
    result = []
    result.append('电子发烧友签到：')
    response = _session.get(
        url=url,
        headers=headers,
    )
    # file = open(file='result.txt', encoding='utf-8', mode='w+')
    # file.write(response.text)
    # file.close()
    formhash = ''
    if response.text.find('<h1>未登录!</h1>') >= 0:
        result.append('未登录')
    elif response.text.find('<h1 class="mt">您今天已经签到过了或者签到时间还未开始</h1>') >= 0:
        result.append('已签到')
    else:
        dom = etree.HTML(response.text.encode())
        elements = dom.xpath('//form/div/input[@name="formhash"]')
        if len(elements):
            formhash = elements[0].xpath('@value')[0]

    # post data
    if len(formhash) > 0:
        url = 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1'
        obj = {
            'formhash': formhash,
            'qdxq': 'kx',
            'qdmode': '3',
            'todaysay': '',
            'fastreply': '0'
        }
        headers['content-type'] = 'application/x-www-form-urlencoded'
        response = _session.post(
            url=url,
            data=obj,
            headers=headers,
            # verify=False
        )

        # file = open(file='result.txt', encoding=response.encoding, mode='w+')
        # file.write(response.text)
        # file.close()

        dom = etree.HTML(response.text.replace('\r\n', ''))
        elements = dom.xpath('//body/div[@id="wp"]/div/div/div')
        if len(elements):
            text = elements[0].xpath('string(.)')
            result.append(text)

    result.append('')
    print('\n'.join(result))


def parse_cookie(cookie_text):
    cookie = dict()
    list = filter(None, cookie_text.split(';'))
    for item in list:
        kv = item.split('=')
        key = kv[0]
        value = ''
        if len(kv) > 1:
            value = kv[1]
        cookie[key] = value
    return cookie


if __name__ == "__main__":
    main()
