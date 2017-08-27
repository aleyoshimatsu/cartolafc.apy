# encoding: utf-8

import requests
from .errors import CartolaFCError
from.util import convert_json_to_data


class RequiresAuthentication(object):

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        self.instance = instance
        return self

    def __call__(self, *args, **kwargs):
        if not self.instance.get_glb_id():
            raise CartolaFCError('Esta função requer autenticação')
        self.func(*args, **kwargs)


class Api(object):

    def __init__(self, email, password):
        self._api_url = 'https://api.cartolafc.globo.com'
        self._auth_url = 'https://login.globo.com/api/authentication'
        self._email = email
        self._password = password
        self._glb_id = None
        self._attempts = 5

    @property
    def get_glb_id(self):
        return self._glb_id

    def login(self):
        response = requests.post(self._auth_url,
                                 json=dict(payload=dict(email=self._email, password=self._password, serviceId=4728)))
        body = response.json()
        if response.status_code == 200:
            self._glb_id = body['glbId']
            return True

        raise CartolaFCError(body['userMessage'])

    def obter_time_logado(self):
        url = "{api_url}/auth/time".format(api_url=self._api_url)
        data = self._request(url)

    def _request(self, url, params=None):
        attempts = self._attempts
        while attempts:
            try:
                headers = {'X-GLB-Token': self._glb_id} if self._glb_id else None
                response = requests.get(url, params=params, headers=headers)
                if self._glb_id and response.status_code == 401:
                    self.login()
                    response = requests.get(url, params=params, headers={'X-GLB-Token': self._glb_id})
                return convert_json_to_data(response.content.decode('utf-8'))
            except CartolaFCError as error:
                attempts -= 1
                if not attempts:
                    raise error
