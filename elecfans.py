import os
import requests

cookie = os.environ["COOKIE"]


def main():
    url = 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign&4726590&infloat=yes&handlekey=dsu_paulsign&inajax=1&ajaxtarget=fwin_content_dsu_paulsign'
    referer = 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign'
    res = get(url, referer)

    result = []
    result.append('电子发烧友签到：')
    result.append(str(res))
    result.append('')

    print('\n'.join(result))


def get(url: str, referer: str):
    headers = {
        'Cookie': cookie,
        'Referer': referer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    res = {}
    try:
        response = requests.get(url, headers=headers)
        res = response.text
    except requests.ConnectionError as e:
        print('Error:', e.args)  # 输出异常信息
    return res


if __name__ == "__main__":
    main()
