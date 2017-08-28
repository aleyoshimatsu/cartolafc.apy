# encoding: utf-8

import requests
from .errors import CartolaFCError
from.util import convert_json_to_data
from .models import Atleta, Clube, Posicao, AtletaStatus


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


MERCADO_ABERTO = 1
MERCADO_FECHADO = 2


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
        posicoes = dict()

        for data_posicao in data_posicoes:
            posicao = Posicao(id=data_posicao['id'],
                              nome=data_posicao['nome'],
                              abreviacao=data_posicao['abreviacao'])
            posicoes[data_posicao['id']] = posicao

        # Parsing Status Atleta
        data_status = data['status'].values()
        atleta_status = dict()

        for data_st in data_status:
            st = AtletaStatus(id=data_st['id'], nome=data_st['nome'])
            atleta_status[data_st['id']] = st

        # Parsing clubes
        data_clubes = data['clubes'].values()
        clubes = dict()

        for data_clube in data_clubes:
            clube = Clube(id=data_clube['id'],
                          nome=data_clube['nome'],
                          abreviacao=data_clube['abreviacao'],
                          posicao=data_clube['posicao'],
                          escudos=data_clube['escudos'])
            clubes[data_clube['id']] = clube

        # Parsing atletas
        data_atletas = data['atletas']
        atletas = list()

        for data_atleta in data_atletas:
            atleta = Atleta(nome=data_atleta['nome'],
                            apelido=data_atleta['apelido'],
                            foto=data_atleta['foto'],
                            atleta_id=data_atleta['atleta_id'],
                            rodada_id=data_atleta['rodada_id'],
                            clube=clubes[data_atleta['clube_id']],
                            posicao=posicoes[data_atleta['posicao_id']],
                            status=atleta_status[data_atleta['status_id']],
                            pontos_num=data_atleta['pontos_num'],
                            preco_num=data_atleta['preco_num'],
                            variacao_num=data_atleta['variacao_num'],
                            media_num=data_atleta['media_num'],
                            jogos_num=data_atleta['jogos_num'],
                            scout=data_atleta['scout'])
            atletas.append(atleta)




    def obter_status_mercado(self):
        url = '{api_url}/mercado/status'.format(api_url=self._api_url)
        data = self._request(url)

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
