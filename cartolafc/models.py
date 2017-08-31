# encoding: utf-8


class Time(object):
    pass


class AtletaStatus(object):

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return "{id}-{nome}".format(id=self.id, nome=self.nome)

    @classmethod
    def parse_json(cls, data):
        return cls(id=data['id'], nome=data['nome'])


class MercadoStatus(object):

    MERCADO_ABERTO = 1
    MERCADO_FECHADO = 2

    def __init__(self, rodada_atual, status_mercado, esquema_default_id, cartoleta_inicial, max_ligas_free,
                 max_ligas_pro, max_ligas_matamata_free, max_ligas_matamata_pro, max_ligas_patrocinadas_free,
                 max_ligas_patrocinadas_pro_num, game_over, temporada, reativar, times_escalados, fechamento,
                 mercado_pos_rodada, aviso, aviso_url):
        self.rodada_atual = rodada_atual
        self.status_mercado = status_mercado
        self.esquema_default_id = esquema_default_id
        self.cartoleta_inicial = cartoleta_inicial
        self.max_ligas_free = max_ligas_free
        self.max_ligas_pro = max_ligas_pro
        self.max_ligas_matamata_free = max_ligas_matamata_free
        self.max_ligas_matamata_pro = max_ligas_matamata_pro
        self.max_ligas_patrocinadas_free = max_ligas_patrocinadas_free
        self.max_ligas_patrocinadas_pro_num = max_ligas_patrocinadas_pro_num
        self.game_over = game_over
        self.temporada = temporada
        self.reativar = reativar
        self.times_escalados = times_escalados
        self.fechamento = fechamento
        self.mercado_pos_rodada = mercado_pos_rodada
        self.aviso = aviso
        self.aviso_url = aviso_url

    def __str__(self):
        return "Rodada: {rodada_atual} - {status_mercado}".format(rodada_atual=self.rodada_atual,
                                                                  status_mercado=self.status_mercado)

    @classmethod
    def parse_json(cls, data):
        return cls(
            rodada_atual=data['rodada_atual'],
            status_mercado=data['status_mercado'],
            esquema_default_id=data['esquema_default_id'],
            cartoleta_inicial=data['cartoleta_inicial'],
            max_ligas_free=data['max_ligas_free'],
            max_ligas_pro=data['max_ligas_pro'],
            max_ligas_matamata_free=data['max_ligas_matamata_free'],
            max_ligas_matamata_pro=data['max_ligas_matamata_pro'],
            max_ligas_patrocinadas_free=data['max_ligas_patrocinadas_free'],
            max_ligas_patrocinadas_pro_num=data['max_ligas_patrocinadas_pro_num'],
            game_over=data['game_over'],
            temporada=data['temporada'],
            reativar=data['reativar'],
            times_escalados=data['times_escalados'],
            fechamento=data['fechamento'],
            mercado_pos_rodada=data['mercado_pos_rodada'],
            aviso=data['aviso'],
            aviso_url=data['aviso_url']
        )

class Posicao(object):

    def __init__(self, id, nome, abreviacao):
        self.id = id
        self.nome = nome
        self.abreviacao = abreviacao

    def __str__(self):
        return "{id}-{nome}".format(id=self.id, nome=self.nome)

    @classmethod
    def parse_json(cls, data):
        return cls(id=data['id'], nome=data['nome'], abreviacao=data['abreviacao'])


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

    def __str__(self):
        return "{id}-{apelido}".format(id=self.atleta_id, apelido=self.apelido)

    @classmethod
    def parse_json(cls, data, clubes, posicoes, atleta_status):
        return cls(nome=data['nome'], apelido=data['apelido'], foto=data['foto'], atleta_id=data['atleta_id'],
                   rodada_id=data['rodada_id'], clube=clubes[data['clube_id']], posicao=posicoes[data['posicao_id']],
                   status=atleta_status[data['status_id']], pontos_num=data['pontos_num'], preco_num=data['preco_num'],
                   variacao_num=data['variacao_num'], media_num=data['media_num'], jogos_num=data['jogos_num'],
                   scout=data['scout'])


class Clube(object):

    def __init__(self, id, nome, abreviacao, posicao, escudos):
        self.id = id
        self.nome = nome
        self.abreviacao = abreviacao
        self.posicao = posicao
        self.escudos = escudos

    def __str__(self):
        return "{id}-{nome}".format(id=self.id, nome=self.nome)

    @classmethod
    def parse_json(cls, data):
        return cls(id=data['id'], nome=data['nome'], abreviacao=data['abreviacao'],
                   posicao=data['posicao'], escudos=data['escudos'])


class Time(object):

    def __init__(self, time_id, clube, esquema_id, cadun_id, facebook_id, foto_perfil, nome, nome_cartola, slug,
                 tipo_escudo, cor_fundo_escudo, cor_borda_escudo, cor_primaria_estampa_escudo,
                 cor_secundaria_estampa_escudo, url_escudo_svg, url_escudo_png, url_camisa_svg,
                 url_camisa_png, url_escudo_placeholder_png, url_camisa_placeholder_png, tipo_estampa_escudo,
                 tipo_adorno, tipo_camisa, tipo_estampa_camisa, cor_camisa, cor_primaria_estampa_camisa,
                 cor_secundaria_estampa_camisa, rodada_time_id, assinante, cadastro_completo, patrocinador1_id,
                 patrocinador2_id, temporada_inicial, simplificado):
        self.time_id = time_id
        self.clube = clube
        self.esquema_id = esquema_id
        self.cadun_id = cadun_id
        self.facebook_id = facebook_id
        self.foto_perfil = foto_perfil
        self.nome = nome
        self.nome_cartola = nome_cartola
        self.slug = slug
        self.tipo_escudo = tipo_escudo
        self.cor_fundo_escudo = cor_fundo_escudo
        self.cor_borda_escudo = cor_borda_escudo
        self.cor_primaria_estampa_escudo = cor_primaria_estampa_escudo
        self.cor_secundaria_estampa_escudo = cor_secundaria_estampa_escudo
        self.url_escudo_svg = url_escudo_svg
        self.url_escudo_png = url_escudo_png
        self.url_camisa_svg = url_camisa_svg
        self.url_camisa_png = url_camisa_png
        self.url_escudo_placeholder_png = url_escudo_placeholder_png
        self.url_camisa_placeholder_png = url_camisa_placeholder_png
        self.tipo_estampa_escudo = tipo_estampa_escudo
        self.tipo_adorno = tipo_adorno
        self.tipo_camisa = tipo_camisa
        self.tipo_estampa_camisa = tipo_estampa_camisa
        self.cor_camisa = cor_camisa
        self.cor_primaria_estampa_camisa = cor_primaria_estampa_camisa
        self.cor_secundaria_estampa_camisa = cor_secundaria_estampa_camisa
        self.rodada_time_id = rodada_time_id
        self.assinante = assinante
        self.cadastro_completo = cadastro_completo
        self.patrocinador1_id = patrocinador1_id
        self.patrocinador2_id = patrocinador2_id
        self.temporada_inicial = temporada_inicial
        self.simplificado = simplificado

    def __str__(self):
        return "{time_id}-{nome}".format(id=self.time_id, nome=self.nome)

    @classmethod
    def parse_json(cls, data, clubes):
        return cls(
            time_id=data['time_id'],
            clube=clubes[data['clube_id']],
            esquema_id=data['esquema_id'],
            cadun_id=data['cadun_id'],
            facebook_id=data['facebook_id'],
            foto_perfil=data['foto_perfil'],
            nome=data['nome'],
            nome_cartola=data['nome_cartola'],
            slug=data['slug'],
            tipo_escudo=data['tipo_escudo'],
            cor_fundo_escudo=data['cor_fundo_escudo'],
            cor_borda_escudo=data['cor_borda_escudo'],
            cor_primaria_estampa_escudo=data['cor_primaria_estampa_escudo'],
            cor_secundaria_estampa_escudo=data['cor_secundaria_estampa_escudo'],
            url_escudo_svg=data['url_escudo_svg'],
            url_escudo_png=data['url_escudo_png'],
            url_camisa_svg=data['url_camisa_svg'],
            url_camisa_png=data['url_camisa_png'],
            url_escudo_placeholder_png=data['url_escudo_placeholder_png'],
            url_camisa_placeholder_png=data['url_camisa_placeholder_png'],
            tipo_estampa_escudo=data['tipo_estampa_escudo'],
            tipo_adorno=data['tipo_adorno'],
            tipo_camisa=data['tipo_camisa'],
            tipo_estampa_camisa=data['tipo_estampa_camisa'],
            cor_camisa=data['cor_camisa'],
            cor_primaria_estampa_camisa=data['cor_primaria_estampa_camisa'],
            cor_secundaria_estampa_camisa=data['cor_secundaria_estampa_camisa'],
            rodada_time_id=data['rodada_time_id'],
            assinante=data['assinante'],
            cadastro_completo=data['cadastro_completo'],
            patrocinador1_id=data['patrocinador1_id'],
            patrocinador2_id=data['patrocinador2_id'],
            temporada_inicial=data['temporada_inicial'],
            simplificado=data['simplificado']
        )


class Servico(object):

    def __init__(self, servicoId, status):
        self.servicoId = servicoId
        self.status = status

    def __str__(self):
        return "{servicoId}-{status}".format(servicoId=self.servicoId, status=self.status)

    @classmethod
    def parse_json(cls, data):
        return cls(data['servicoId'], data['status'])


class TimeInfo(object):

    def __init__(self, atletas, clubes, posicoes, atleta_status, time, patrimonio, esquema_id, pontos, valor_time,
                 rodada_atual, variacao_patrimonio, variacao_pontos, servicos, total_ligas, total_ligas_matamata):
        self.atletas = atletas
        self.clubes = clubes
        self.posicoes = posicoes
        self.atleta_status = atleta_status
        self.time = time
        self.patrimonio = patrimonio
        self.esquema_id = esquema_id
        self.pontos = pontos
        self.valor_time = valor_time
        self.rodada_atual = rodada_atual
        self.variacao_patrimonio = variacao_patrimonio
        self.variacao_pontos = variacao_pontos
        self.servicos = servicos
        self.total_ligas = total_ligas
        self.total_ligas_matamata = total_ligas_matamata

    def __str__(self):
        return "{time_id}-{nome}".format(time_id=self.time.time_id, nome=self.time.nome)

    @classmethod
    def parse_json(cls, data, atletas, clubes, posicoes, atleta_status, time):
        return cls(
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
            servicos=[Servico.parse_json(data_servico) for data_servico in data['servicos']],
            total_ligas=data['total_ligas'],
            total_ligas_matamata=data['total_ligas_matamata']
        )


class AtletaPontuacao(object):

    def __init__(self, atleta_id, rodada_id, pontos, preco, variacao, media):
        self.atleta_id = atleta_id
        self.rodada_id = rodada_id
        self.pontos = pontos
        self.preco = preco
        self.variacao = variacao
        self.media = media

    def __str__(self):
        return "{atleta_id}-{nome}".format(atleta_id=self.atleta_id, nome=self.time.nome)

    @classmethod
    def parse_json(cls, data):
        return cls(data['atleta_id'], data['rodada_id'], data['pontos'], data['preco'], data['variacao'], data['media'])


class AtletaPontuado(object):

    def __init__(self, apelido, pontuacao, scout, foto, posicao_id, clube_id):
        self.apelido = apelido
        self.pontuacao = pontuacao
        self.scout = scout
        self.foto = foto
        self.posicao_id = posicao_id
        self.clube_id = clube_id

    def __str__(self):
        return "{apelido}={pontuacao}".format(apelido=self.apelido, pontuacao=self.pontuacao)

    @classmethod
    def parse_json(cls, data):
        return cls(data['apelido'], data['pontuacao'], data['scout'],
                   data['foto'], data['posicao_id'], data['clube_id'])
