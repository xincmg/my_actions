import requests
from requests.adapters import HTTPAdapter


class SiteBase:

    def __init__(self, flag, user):        
        self._user = user
        self._flag = flag
        self._state = 'running...'
        self._session = requests.Session()
        self._session.mount('http://', HTTPAdapter(max_retries=5))
        self._session.mount('https://', HTTPAdapter(max_retries=5))
        self._session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        })

    @property
    def flag(self):
        return self._flag

    @property
    def user(self):
        return self._user

    @property
    def session(self):
        return self._session
    
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def result(self):        
        return f'{self.flag}：{self.user.name}\n{self.state}\n'

    def signin(self):
        '''签到实现'''
        raise NotImplementedError
    
    def report(self):
        '''解析返回的结果'''
        raise NotImplementedError

    def login(self):
        '''将登录状态保持在会话中'''
        raise NotImplementedError

    def run(self):
        self.login()
        response = self.signin()
        if response is None:
            return
        self.report(response)
