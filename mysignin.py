import json
import os
from importlib import import_module

from helper import readtext
from user import User

try:
    account_text = os.environ["ACCOUNTS"]
except:
    account_text = readtext('.private\\account.json')


def run():
    result = []
    accounts = json.loads(account_text)
    for account in accounts:
        name = account['uid']
        token = account['token']
        flag = account["flag"]
        if not name or not token or not flag:            
            continue
        # if flag != 'Oshwhub':
        #     continue
        user = User(name, token)
        # 导入类
        try:
            module = import_module(f'sites.{flag.lower()}')
            obj = getattr(module, flag)
        except (ModuleNotFoundError, AttributeError) as e:
            print(e)
            continue
        site = obj(flag, user)
        try:
            site.run()
        except(Exception) as e:
            print(e)
            # pass
        result.append(site.result)
    print('\n'.join(result))


if __name__ == '__main__':
    run()
