# encoding: utf-8
from cartolafc.api import Api
from cartolafc.errors import CartolaFCError


def test_login_sucesso():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    assert api.login()


def test_login_erro():
    api = Api(email="aleyoshimatsu@gmail.comm", password="yoshi123")
    try:
        api.login()
    except CartolaFCError as ex:
        assert ex.__str__() == "Seu e-mail ou senha estão incorretos."


def test_obter_time_logado():
    api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
    api.login()
    time_info = api.obter_time_logado()
    assert True


# def test_obter_parciais():
#     api = Api(email="aleyoshimatsu@gmail.com", password="yoshi123")
#     api.login()
#     api.obter_parciais()
#     assert True
