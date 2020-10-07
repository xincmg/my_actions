import os
import time

import requests

cookie = os.environ["COOKIE"]


def main():
    # 签到
    result = []
    result.append('360有钱签到：')
    ts = int(time.time() * 1000)
    url = f'http://youqian.360.cn/sign/sign?t={ts}'
    referer = 'http://youqian.360.cn/score.html'
    res = get(url, referer)
    if res['errno'] == 12:
        result.append('未登录')
    elif res['errno'] == 0:
        try:
            info = res['errmsg'] + '，积分：' + res['data']['score_available'] + '，连续签到' + res['data']['user_info'][
                'continous_day'] + '天'
            result.append(info)
        except:
            result.append('json结构不符合预期')
    elif res['errno'] == 1:
        result.append('已经签到')
    result.append(str(res))

    # 安全盾签到
    result.append('')
    result.append('安全盾签到：')
    ts = int(time.time() * 1000)
    url = f'http://youqian.360.cn/task/finishtask?type=1&t={ts}'
    referer = 'http://youqian.360.cn/task.html'
    res = get(url, referer)
    if res:
        if res['errno'] == 12:
            result.append('未登录')
        else:
            info = res['errmsg'] + '，安全盾：' + res['data']['num'] + '个'
            result.append(info)
    result.append(str(res))
    print('\n'.join(result))


def get(url: str, referer: str):
    headers = {
        'Cookie': cookie,
        'Host': 'youqian.360.cn',
        'Referer': referer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
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
