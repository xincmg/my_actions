from lxml import etree
import requests


cookie = 'visitor=0b721e7d2579fc75073dadf9a4cf6927; rlhx_e495_saltkey=BPlhpLdh; rlhx_e495_lastvisit=1628734663; auth_bbs=43EFkU3XSdG3THbL%252FuRYK8%252FqxecTq6pJaE5bDdsP6MKw2tk57qatFOaogZrw2HorrU1kEsOfSC%252FjSdr7ppy12gbgVHiPQyOX7TsgrH%252BLgiJOBj3tad%252BXXimvKOxPDrk4E3EvCxxBO0YbARtJIjMGCnb1wPmT33TyafDxMjccrThB1NJrv%252FXE06YALkKptCk9ln3HKkKTsTAuWNqHBbwo3jLtgGPSNgeLPwVFBYK8pbvvshDDV3AkPpC4oe%252BHhNep%252BS5Um7AYYlKrlnWDfGjp%252FLMaGBES3AHzHfZs2V%252BSXzxartISny6v3OhwOlniU%252BmjN4rLU%252FwK5HgVWZw1t%252FivO6ZG%252FfRaD42QdtmjIa6%252FT%252FIvnEShFLPaVcxBlP0eb68smguG1iXJKz5V%252B8W%252BaZ%252BXj0AolZP5fEboTz4q3deySZNIJfK1TA7Ev67c3KrPFiWUDQm9iSjNetWAR9sviREvQg; auth_www=Y5bQcnbuS6aaxZ7m3FYd1REF5iFcJpLiuSgozcKPIhX%252FvbNc9K5s5fBZKp5TO0Ss78YrJfORGmTCXoYyumesX3YvA9BaZ120FHKOo8qhcRxfK5IRe5SWLbk49K7jkxi5nLJHu6YO3k76N%252FBZPfW%252FyuL5o4zEGRaftkPYkUIU%252FM9fGm2PAeQjCfXV1wvPgqJh%252BibY8mGA80%252BS5r0M9RSF%252Fglte1PZEjA%252FwurFGrXdCUUom0FDtJH4q9gCzQ%252BITcevqyHimpO%252BBgjehPiY8r9XDHWzDkNwqgRKpLh3vtekkM5SbtO%252FLg%252FmyPEqPoVYFEdUp%252B8BkZ7ViFxIpZ1cPPh%252F1Gfm1gYKunxZtcxExuymFcfE4dYhD9ipowmAp5D%252BJFzQ6n4IaCWksXsz4gFbIEEGgaIHTbqH1Ho0Wq44vjdFZHE7tEshUxqSTwMh99v0XDT5HKa99UnMo%252ByjncbgnW6luQ; rlhx_e495_atarget=1; DedeLoginTime=1628933942; DedeLoginTime__ckMd5=7ad7dae83a3aaef0; rlhx_e495_forum_lastvisit=D_76_1628745076D_10_1628950400D_84_1628950496; rlhx_e495_smile=1D1; rlhx_e495_taskdoing_4726590=1; rlhx_e495_visitedfid=49D686D76D830D55D25D51D888D1403D1412; rlhx_e495_ulastactivity=14a7X06IrF4ATZU4KwURuMC8rfHEgKnowKHhIf7%2BJIr4mOivI4e%2F; acw_tc=af06eb9d16295241854482010e25b437766796605e5f642040caf33bb1; rlhx_e495_sid=odDqJv; rlhx_e495_lip=27.24.15.95%2C1629524177; rlhx_e495_onlineusernum=9889; rlhx_e495_sendmail=1; rlhx_e495_home_diymode=1; rlhx_e495_lastcheckfeed=4726590%7C1629524360; rlhx_e495_checkfollow=1; rlhx_e495_checkpm=1; rlhx_e495_lastact=1629524365%09misc.php%09nav'
# cookie = os.environ["COOKIE"]
cookie = 'auth_bbs=43EFkU3XSdG3THbL%252FuRYK8%252FqxecTq6pJaE5bDdsP6MKw2tk57qatFOaogZrw2HorrU1kEsOfSC%252FjSdr7ppy12gbgVHiPQyOX7TsgrH%252BLgiJOBj3tad%252BXXimvKOxPDrk4E3EvCxxBO0YbARtJIjMGCnb1wPmT33TyafDxMjccrThB1NJrv%252FXE06YALkKptCk9ln3HKkKTsTAuWNqHBbwo3jLtgGPSNgeLPwVFBYK8pbvvshDDV3AkPpC4oe%252BHhNep%252BS5Um7AYYlKrlnWDfGjp%252FLMaGBES3AHzHfZs2V%252BSXzxartISny6v3OhwOlniU%252BmjN4rLU%252FwK5HgVWZw1t%252FivO6ZG%252FfRaD42QdtmjIa6%252FT%252FIvnEShFLPaVcxBlP0eb68smguG1iXJKz5V%252B8W%252BaZ%252BXj0AolZP5fEboTz4q3deySZNIJfK1TA7Ev67c3KrPFiWUDQm9iSjNetWAR9sviREvQg'
headers = {
    'Cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded'
}
_session = requests.Session()


def main():
    # get formhash
    url = 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign&4726590&infloat=yes&handlekey=dsu_paulsign&inajax=1&ajaxtarget=fwin_content_dsu_paulsign'
    headers['Referer'] = 'https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign'

    result = []
    result.append('电子发烧友签到：')
    response = _session.get(url, headers=headers)
    file = open(file='result.txt', encoding='utf-8', mode='w+')
    file.write(response.text)
    file.close()
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
        # formhash=90206f7c&qdxq=kx&qdmode=3&todaysay=&fastreply=0
        # obj = f'formhash={formhash}&qdxq=kx&qdmode=3&todaysay=&fastreply=0'
        response = _session.post(url=url, data=obj,headers=headers)
        file = open(file='result.txt', encoding='utf-8', mode='w+')
        file.write(response.text)
        file.close()

    result.append('')
    print('\n'.join(result))

def get(url: str, referer: str):
    res = {}
    try:
        response = requests.get(url, headers=headers)
        res = response.text
    except requests.ConnectionError as e:
        print('Error:', e.args)  # 输出异常信息
    return res


if __name__ == "__main__":
    main()
