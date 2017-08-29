# encoding: utf-8

import requests
from .errors import CartolaFCError
from.util import convert_json_to_data
from .models import Atleta, Clube, Posicao, AtletaStatus, Time, TimeInfo, Servico


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
        time = Time(
            time_id=data_time['time_id'],
            clube=clubes[data_time['clube_id']],
            esquema_id=data_time['esquema_id'],
            cadun_id=data_time['cadun_id'],
            facebook_id=data_time['facebook_id'],
            foto_perfil=data_time['foto_perfil'],
            nome=data_time['nome'],
            nome_cartola=data_time['nome_cartola'],
            slug=data_time['slug'],
            tipo_escudo=data_time['tipo_escudo'],
            cor_fundo_escudo=data_time['cor_fundo_escudo'],
            cor_borda_escudo=data_time['cor_borda_escudo'],
            cor_primaria_estampa_escudo=data_time['cor_primaria_estampa_escudo'],
            cor_secundaria_estampa_escudo=data_time['cor_secundaria_estampa_escudo'],
            url_escudo_svg=data_time['url_escudo_svg'],
            url_escudo_png=data_time['url_escudo_png'],
            url_camisa_svg=data_time['url_camisa_svg'],
            url_camisa_png=data_time['url_camisa_png'],
            url_escudo_placeholder_png=data_time['url_escudo_placeholder_png'],
            url_camisa_placeholder_png=data_time['url_camisa_placeholder_png'],
            tipo_estampa_escudo=data_time['tipo_estampa_escudo'],
            tipo_adorno=data_time['tipo_adorno'],
            tipo_camisa=data_time['tipo_camisa'],
            tipo_estampa_camisa=data_time['tipo_estampa_camisa'],
            cor_camisa=data_time['cor_camisa'],
            cor_primaria_estampa_camisa=data_time['cor_primaria_estampa_camisa'],
            cor_secundaria_estampa_camisa=data_time['cor_secundaria_estampa_camisa'],
            rodada_time_id=data_time['rodada_time_id'],
            assinante=data_time['assinante'],
            cadastro_completo=data_time['cadastro_completo'],
            patrocinador1_id=data_time['patrocinador1_id'],
            patrocinador2_id=data_time['patrocinador2_id'],
            temporada_inicial=data_time['temporada_inicial'],
            simplificado=data_time['simplificado']
        )

        # Parsing time info
        time_info = TimeInfo(
            atletas=atletas,
            clubes=clubes,
            posicoes=posicoes,
            atleta_status=atleta_status,
            time=time,
            patrimonio=data['patrimonio'],
            esquema_id=data['esquema_id'],
            pontos=data['pontos'],
            valor_time=data['valor_time'],
            rodada_atual=data['rodada_atual'],
            variacao_patrimonio=data['variacao_patrimonio'],
            variacao_pontos=data['variacao_pontos'],
            servicos=[Servico(data_servico['servicoId'], data_servico['status']) for data_servico in data['servicos']],
            total_ligas=data['total_ligas'],
            total_ligas_matamata=data['total_ligas_matamata']
        )

        return time_info


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
