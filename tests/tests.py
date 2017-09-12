# encoding: utf-8
from cartolafc.api import Api
from cartolafc.errors import CartolaFCError
from cartolafc.models import MercadoStatus


def test_login_sucesso():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    assert api.login()


def test_login_erro():
    api = Api(email="aleyoshimatsu@gmail.comm", password="yoshi123")
    try:
        api.login()
        assert True
    except CartolaFCError as ex:
        assert ex.__str__() == "Seu e-mail ou senha estão incorretos."


def test_obter_time_logado():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    api.login()
    time_info = api.obter_time_logado()
    assert True


def test_obter_status_mercado():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    api.login()
    mercado_status = api.obter_status_mercado()
    assert mercado_status.status_mercado == MercadoStatus.MERCADO_ABERTO


def test_obter_atleta_pontuacao():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    api.login()
    atleta_pontuacao = api.obter_atleta_pontuacao(id=81905)
    assert True


def test_obter_atleta_pontuados():
    try:
        api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
        api.login()
        api.obter_atleta_pontuados()
        assert True
    except CartolaFCError as ex:
        assert ex.__str__() == "Pontuações parciais indisponíveis! Mercado aberto."


def test_obter_ligas_time_logado():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    api.login()
    ligas = api.obter_ligas_time_logado()
    assert len(ligas) > 0


def test_obter_liga_by_slug():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    api.login()
    liga = api.obter_liga_by_slug(slug='liga-showbol-2017')
    assert liga.slug == 'liga-showbol-2017'


def test_obter_time_by_slug():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    api.login()
    time_info = api.obter_time_by_slug(slug='santastico-yoshi-f-c')
    assert time_info.time_usuario.slug == 'santastico-yoshi-f-c'
