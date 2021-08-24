import os
from lxml import etree
import requests

# cookie = 'EFmf_2132_saltkey=g40c8Ecc;EFmf_2132_auth=f594Z4jKbkONwsygZHh213FcYub8D0uA7twitR60z25IZ2VFsrBiwBBciMIlfx6N1D3%2F8hcbqdfC48IIaohNxhHBjs8;'
cookie = os.environ["COOKIE"]
headers = {
    'Cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Referer': 'https://www.arduino.cn/plugin.php?id=dsu_paulsign:sign',
    'Host': 'www.arduino.cn',
    'Content-Type': 'application/x-www-form-urlencoded'
}

_session = requests.Session()

def main():
    result = []
    result.append('arduino中文社区签到：')
    url = 'https://www.arduino.cn/plugin.php?id=dsu_paulsign:sign'
    response = _session.get(url=url, headers=headers)
    # file = open(file='result.txt', encoding='utf-8', mode='w+')
    # file.write(response.text)
    # file.close()
    formhash = ''
    if response.text.find('<p>您需要先登录才能继续本操作') >= 0:
        result.append('未登录')
    elif response.text.find('<h1 class="mt">您今天已经签到过了或者签到时间还未开始</h1>') >= 0:
        result.append('已签到')
    else:
        dom = etree.HTML(response.text.encode())
        elements = dom.xpath('//form/input[@name="formhash"]')
        if len(elements):
            formhash = elements[0].xpath('@value')[0]
        else:
            result.append('找不到formhash')

    # post data
    if len(formhash) > 0:
        # result.append(f'formhash is {formhash}')
        url = 'https://www.arduino.cn/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1'
        obj = {
            'formhash': formhash,
            'qdxq': 'kx',
            'qdmode': '3',
            'todaysay': '',
            'fastreply': '0'
        }
        response = _session.post(url=url, data=obj, headers=headers)
        # file = open(file='result.txt', encoding='utf-8', mode='w+')
        # file.write(response.text)
        # file.close()
        dom = etree.HTML(response.text)
        elements = dom.xpath('//body/div[@id="wp"]/div/div')
        if len(elements):
            text = elements[0].xpath('text()')[0].strip()
            result.append(text)
            
    result.append('')
    print('\n'.join(result))


if __name__ == "__main__":
    main()
