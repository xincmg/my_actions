import os
from lxml import etree
import requests

cookie = os.environ["COOKIE"]
# cookie = 'rlhx_e495_saltkey=BPlhpLdh;auth_bbs=43EFkU3XSdG3THbL%252FuRYK8%252FqxecTq6pJaE5bDdsP6MKw2tk57qatFOaogZrw2HorrU1kEsOfSC%252FjSdr7ppy12gbgVHiPQyOX7TsgrH%252BLgiJOBj3tad%252BXXimvKOxPDrk4E3EvCxxBO0YbARtJIjMGCnb1wPmT33TyafDxMjccrThB1NJrv%252FXE06YALkKptCk9ln3HKkKTsTAuWNqHBbwo3jLtgGPSNgeLPwVFBYK8pbvvshDDV3AkPpC4oe%252BHhNep%252BS5Um7AYYlKrlnWDfGjp%252FLMaGBES3AHzHfZs2V%252BSXzxartISny6v3OhwOlniU%252BmjN4rLU%252FwK5HgVWZw1t%252FivO6ZG%252FfRaD42QdtmjIa6%252FT%252FIvnEShFLPaVcxBlP0eb68smguG1iXJKz5V%252B8W%252BaZ%252BXj0AolZP5fEboTz4q3deySZNIJfK1TA7Ev67c3KrPFiWUDQm9iSjNetWAR9sviREvQg;'
headers = {
    'Cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Referer': 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign',
    # 'Host': 'bbs.elecfans.com',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}
_session = requests.Session()


def main():
    # get formhash
    url = 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign&4726590&infloat=yes&handlekey=dsu_paulsign&inajax=1&ajaxtarget=fwin_content_dsu_paulsign'

    result = []
    result.append('电子发烧友签到：')
    response = _session.get(url, headers=headers)
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
        result.append(f'formhash is {formhash}')
        url = 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1'
        obj = {
            'formhash': formhash,
            'qdxq': 'kx',
            'qdmode': '3',
            'todaysay': '',
            'fastreply': '0'
        }
        # headers['content-type'] = 'application/x-www-form-urlencoded'
        response = _session.post(
            url=url, data=obj, headers=headers)
        # file = open(file='result.txt', encoding='utf-8', mode='w+')
        # file.write(response.text)
        # file.close()
        dom = etree.HTML(response.text)
        elements = dom.xpath('//body/div[@id="wp"]/div/div/div')
        if len(elements):
            text = elements[0].xpath('string(.)')
            result.append(text)

    result.append('\n\n')
    print('\n'.join(result))


if __name__ == "__main__":
    main()
