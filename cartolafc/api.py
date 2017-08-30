# encoding: utf-8

import requests
from .errors import CartolaFCError
from.util import convert_json_to_data
from .models import Atleta, Clube, Posicao, AtletaStatus, Time, TimeInfo, MercadoStatus


class RequiresAuthentication(object):

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        self.instance = instance
        return self

    def __call__(self, *args, **kwargs):
        if not self.instance.is_logged():
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

    def is_logged(self):
        return self._glb_id is not None

    def login(self):
        response = requests.post(self._auth_url,
                                 json=dict(payload=dict(email=self._email, password=self._password, serviceId=4728)))
        body = response.json()
        if response.status_code == 200:
            self._glb_id = body['glbId']
            return True

        raise CartolaFCError(body['userMessage'])

    # @RequiresAuthentication
    def obter_time_logado(self):
        url = "{api_url}/auth/time".format(api_url=self._api_url)
        data = self._request(url)

        # Parsing Posicao
        data_posicoes = data['posicoes'].values()
        posicoes = dict((data_posicao['id'], Posicao.parse_json(data_posicao)) for data_posicao in data_posicoes)

        # Parsing Status Atleta
        data_status = data['status'].values()
        atleta_status = dict((data_st['id'], AtletaStatus.parse_json(data_st)) for data_st in data_status)

        # Parsing clubes
        data_clubes = data['clubes'].values()
        clubes = dict((data_clube['id'], Clube.parse_json(data_clube)) for data_clube in data_clubes)

        # Parsing atletas
        data_atletas = data['atletas']
        atletas = list(Atleta.parse_json(data_atleta, clubes, posicoes, atleta_status) for data_atleta in data_atletas)

        # Parsing time
        data_time = data['time']
        time = Time.parse_json(data_time, clubes)

        # Parsing time info
        time_info = TimeInfo.parse_json(data, atletas, clubes, posicoes, atleta_status, time)

        return time_info

    def obter_status_mercado(self):
        url = '{api_url}/mercado/status'.format(api_url=self._api_url)
        data = self._request(url)

        # Parsing mercado status
        mercado_status = MercadoStatus.parse_json(data)
        return mercado_status

    def obter_parciais(self):
        # if self.mercado().status.id == MERCADO_FECHADO:
            url = '{api_url}/atletas/pontuados'.format(api_url=self._api_url)
            data = self._request(url)

        # raise CartolaFCError('As pontuações parciais só ficam disponíveis com o mercado fechado.')

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
