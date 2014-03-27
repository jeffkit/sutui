#encoding=utf-8

import requests
import time
from hashlib import sha1
import simplejson

VERSION = 0.2


class Sutui(object):
    """
    """
    API_HOST = 'http://api.sutui.me'

    def __init__(self, key, secret, api_host=None):
        self.key = key
        self.secret = secret
        if not api_host:
            self.api_host = self.API_HOST
        else:
            self.api_host = api_host

    def _complete_url(self, url):
        if '?' in url:
            url = url + '&'
        else:
            url = url + '?'
        timestamp = '%.5f' % time.time()
        key = 'api.key=%s' % self.key
        ts = 'api.timestamp=%s' % timestamp
        sign = 'api.signature=%s' % sha1(
            '&'.join((self.key, self.secret, timestamp))).hexdigest()
        return self.api_host + url + '&'.join((key, ts, sign))

    def _process_response(self, rsp):
        if rsp.status_code == 200:
            data = rsp.json()
            if 'errno' in data and data['errno'] != 0:
                return None
            else:
                return data
        else:
            return None

    def subscribe(self, user_id, channel_id, unsubscribe=False):
        data = {'user_id': user_id, 'channel_id': channel_id,
                'unsubscribe': unsubscribe}
        rsp = requests.post(self._complete_url('/subscription/'),
                            data=data)
        return self._process_response(rsp)

    def subscriptions(self, user_id):
        rsp = requests.get(self._complete_url('/subscription/'),
                           params={'user_id': user_id})
        return self._process_response(rsp)

    def channels(self):
        rsp = requests.get(self._complete_url('/channel/'))
        return self._process_response(rsp)

    def create_channel(self, name, identity=None):
        data = {'name': name, 'identity': identity}
        rsp = requests.post(self._complete_url('/channel/'),
                            data=data)
        return self._process_response(rsp)

    def notify(self, channel_id, msg_type, message):
        data = {'channel_id': channel_id, 'msg_type': msg_type,
                'content': message}
        headers = {'Content-type': 'application/json'}
        rsp = requests.post(self._complete_url('/message/'),
                            data=simplejson.dumps(data),
                            headers=headers)
        return self._process_response(rsp)
