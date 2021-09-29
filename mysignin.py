import json
import os
from importlib import import_module

from user import User

account_text=os.environ["ACCOUNTS"]
# file = open('.private\\account.txt', mode='r')
# account_text = file.read()
# file.close()


def run():
    result = []
    accounts = json.loads(account_text)
    for account in accounts:
        name = account['uid']
        token = account['token']
        flag = account["flag"]
        if not name or not token or not flag:
            continue
        user = User(name, token)
        # 导入类
        try:
            module = import_module(f'sites.{flag.lower()}')
            obj = getattr(module, flag)
        except (ModuleNotFoundError, AttributeError) as e:
            print(e)
            continue
        site = obj(flag, user)
        site.run()
        result.append(site.result)
    print('\n'.join(result))


if __name__ == '__main__':
    run()
