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

    result = []
    result.append('pthome签到：')
    if response.text.find('<h1>未登录!</h1>') == -1:
        dom = etree.HTML(response.text)
        etree.strip_tags(dom, 'tbody', 'b', 'p')
        element = dom.xpath("//td[@class='embedded']/table/tr/td/text()")
        result .append(''.join(element).strip())
    else:
        result.append('未登录')

    result.append('')
    result.append('')
    print('\n'.join(result))


if __name__ == "__main__":    
    main()
