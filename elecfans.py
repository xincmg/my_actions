import os
import requests 

# cookie=os.environ["COOKIE"]
cookie=""

def main():
    uid='4726590'
    url=f'https://bbs.elecfans.com/home.php?mod=misc&ac=ajax&op=userDFM&uid={uid}'
    referer='https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign'
    text=[]
    text.append("电子发烧友签到：")
    res= get(url,referer)
    text.append(str(res))
    text.append("")
    print('\n'.join(text))

def get(url: str, referer: str):
    headers = {
        'Cookie': cookie,
        'Referer': referer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'content-type': 'application/json',
    }
    res = {}
    try:
        response = requests.get(url, headers=headers)
        res = response.json()
    except requests.ConnectionError as e:
        print('Error:', e.args)  # 输出异常信息
    return res

if __name__ == "__main__":
    main()