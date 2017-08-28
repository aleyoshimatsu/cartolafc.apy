# encoding: utf-8


class Time(object):
    pass


class AtletaStatus(object):

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class MercadoStatus(object):
    pass


class Posicao(object):

    def __init__(self, id, nome, abreviacao):
        self.id = id
        self.nome = nome
        self.abreviacao = abreviacao


class Atleta(object):

    def __init__(self, nome, apelido, foto, atleta_id, rodada_id, clube, posicao, status, pontos_num, preco_num, variacao_num, media_num, jogos_num, scout):
        self.nome = nome
        self.apelido = apelido
        self.foto = foto
        self.atleta_id = atleta_id
        self.rodada_id = rodada_id
        self.clube = clube
        self.posicao = posicao
        self.status = status
        self.pontos_num = pontos_num
        self.preco_num = preco_num
        self.variacao_num = variacao_num
        self.media_num = media_num
        self.jogos_num = jogos_num
        self.scout = scout


class Clube(object):

    def __init__(self, id, nome, abreviacao, posicao, escudos):
        self.id = id
        self.nome = nome
        self.abreviacao = abreviacao
        self.posicao = posicao
        self.escudos = escudos
