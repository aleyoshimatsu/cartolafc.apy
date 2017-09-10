# encoding: utf-8


class RankingTime(object):

    def __init__(self, rodada, mes, turno, campeonato, patrimonio):
        self.rodada = rodada
        self.mes = mes
        self.turno = turno
        self.campeonato = campeonato
        self.patrimonio = patrimonio

    @classmethod
    def parse_json(cls, data):
        return cls(
            rodada=data['rodada'],
            mes=data['mes'],
            turno=data['turno'],
            campeonato=data['campeonato'],
            patrimonio=data['patrimonio']
        )


class PontosTime(object):

    def __init__(self, rodada, mes, turno, campeonato):
        self.rodada = rodada
        self.mes = mes
        self.turno = turno
        self.campeonato = campeonato

    @classmethod
    def parse_json(cls, data):
        return cls(
            rodada=data['rodada'],
            mes=data['mes'],
            turno=data['turno'],
            campeonato=data['campeonato']
        )


class VariacaoTime(object):

    def __init__(self, mes, turno, campeonato, patrimonio):
        self.mes = mes
        self.turno = turno
        self.campeonato = campeonato
        self.patrimonio = patrimonio

    @classmethod
    def parse_json(cls, data):
        return cls(
            mes=data['mes'],
            turno=data['turno'],
            campeonato=data['campeonato'],
            patrimonio=data['patrimonio']
        )


class Time(object):

    def __init__(self, url_escudo_png, url_escudo_svg, url_placeholder_escudo_png, time_id, nome, nome_cartola, slug,
                 facebook_id, url_escudo_placeholder_png, foto_perfil, assinante, patrimonio,
                 ranking_time, pontos_time, variacao_time):
        self.url_escudo_png = url_escudo_png
        self.url_escudo_svg = url_escudo_svg
        self.url_placeholder_escudo_png = url_placeholder_escudo_png
        self.time_id = time_id
        self.nome = nome
        self.nome_cartola = nome_cartola
        self.slug = slug
        self.facebook_id = facebook_id
        self.url_escudo_placeholder_png = url_escudo_placeholder_png
        self.foto_perfil = foto_perfil
        self.assinante = assinante
        self.patrimonio = patrimonio
        self.ranking_time = ranking_time
        self.pontos_time = pontos_time
        self.variacao_time = variacao_time

    def __str__(self):
        return "{id}-{slug}".format(id=self.time_id, slug=self.slug)

    @classmethod
    def parse_json(cls, data):
        return cls(
            url_escudo_png=data['url_escudo_png'],
            url_escudo_svg=data['url_escudo_svg'],
            url_placeholder_escudo_png=data['url_placeholder_escudo_png'],
            time_id=data['time_id'],
            nome=data['nome'],
            nome_cartola=data['nome_cartola'],
            slug=data['slug'],
            facebook_id=data['facebook_id'],
            url_escudo_placeholder_png=data['url_escudo_placeholder_png'],
            foto_perfil=data['foto_perfil'],
            assinante=data['assinante'],
            patrimonio=data['patrimonio'],
            ranking_time=RankingTime.parse_json(data['ranking']),
            pontos_time=PontosTime.parse_json(data['pontos']),
            variacao_time=VariacaoTime.parse_json(data['variacao'])
        )


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
        return cls(
            nome=data['nome'],
            apelido=data['apelido'],
            foto=data['foto'],
            atleta_id=data['atleta_id'],
            rodada_id=data['rodada_id'],
            clube=clubes[data['clube_id']],
            posicao=posicoes[data['posicao_id']],
            status=atleta_status[data['status_id']],
            pontos_num=data['pontos_num'],
            preco_num=data['preco_num'],
            variacao_num=data['variacao_num'],
            media_num=data['media_num'],
            jogos_num=data['jogos_num'],
            scout=data['scout']
        )


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
        return cls(
            id=data['id'],
            nome=data['nome'],
            abreviacao=data['abreviacao'],
            posicao=data['posicao'],
            escudos=data['escudos']
        )


class TimeUsuario(object):

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

    def __init__(self, atletas, clubes, posicoes, atleta_status, time_usuario, patrimonio, esquema_id, pontos, valor_time,
                 rodada_atual, variacao_patrimonio, variacao_pontos, servicos, total_ligas, total_ligas_matamata):
        self.atletas = atletas
        self.clubes = clubes
        self.posicoes = posicoes
        self.atleta_status = atleta_status
        self.time_usuario = time_usuario
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
        return "{time_id}-{nome}".format(time_id=self.time_usuario.time_id, nome=self.time_usuario.nome)

    @classmethod
    def parse_json(cls, data, atletas, clubes, posicoes, atleta_status, time_usuario):
        return cls(
            atletas=atletas,
            clubes=clubes,
            posicoes=posicoes,
            atleta_status=atleta_status,
            time_usuario=time_usuario,
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
        return cls(
            atleta_id=data['atleta_id'],
            rodada_id=data['rodada_id'],
            pontos=data['pontos'],
            preco=data['preco'],
            variacao=data['variacao'],
            media=data['media']
        )


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
        return cls(
            apelido=data['apelido'],
            pontuacao=data['pontuacao'],
            scout=data['scout'],
            foto=data['foto'],
            posicao_id=data['posicao_id'],
            clube_id=data['clube_id']
        )


class Liga(object):

    def __init__(self, liga_id, time_dono_id, clube_id, nome, descricao, slug, tipo, tipo_flamula, tipo_estampa_flamula,
                 tipo_adorno_flamula, cor_primaria_estampa_flamula, cor_secundaria_estampa_flamula, cor_borda_flamula,
                 cor_fundo_flamula, url_flamula_svg, url_flamula_png, tipo_trofeu, cor_trofeu, url_trofeu_svg,
                 url_trofeu_png, editorial, patrocinador, mata_mata, inicio_rodada, fim_rodada, quantidade_times,
                 sorteada, mes_ranking_num, mes_variacao_num, camp_ranking_num, camp_variacao_num, imagem, amigos,
                 total_amigos_na_liga, total_times_liga):
        self.liga_id = liga_id
        self.time_dono_id = time_dono_id
        self.clube_id = clube_id
        self.nome = nome
        self.descricao = descricao
        self.slug = slug
        self.tipo = tipo
        self.tipo_flamula = tipo_flamula
        self.tipo_estampa_flamula = tipo_estampa_flamula
        self.tipo_adorno_flamula = tipo_adorno_flamula
        self.cor_primaria_estampa_flamula = cor_primaria_estampa_flamula
        self.cor_secundaria_estampa_flamula = cor_secundaria_estampa_flamula
        self.cor_borda_flamula = cor_borda_flamula
        self.cor_fundo_flamula = cor_fundo_flamula
        self.url_flamula_svg = url_flamula_svg
        self.url_flamula_png = url_flamula_png
        self.tipo_trofeu = tipo_trofeu
        self.cor_trofeu = cor_trofeu
        self.url_trofeu_svg = url_trofeu_svg
        self.url_trofeu_png = url_trofeu_png
        self.editorial = editorial
        self.patrocinador = patrocinador
        self.mata_mata = mata_mata
        self.inicio_rodada = inicio_rodada
        self.fim_rodada = fim_rodada
        self.quantidade_times = quantidade_times
        self.sorteada = sorteada
        self.mes_ranking_num = mes_ranking_num
        self.mes_variacao_num = mes_variacao_num
        self.camp_ranking_num = camp_ranking_num
        self.camp_variacao_num = camp_variacao_num
        self.imagem = imagem
        self.amigos = amigos
        self.total_amigos_na_liga = total_amigos_na_liga
        self.total_times_liga = total_times_liga

    def __str__(self):
        return "{liga_id}={nome}".format(liga_id=self.liga_id, nome=self.nome)

    @classmethod
    def parse_json(cls, data, amigos = None):
        return cls(
            liga_id=data["liga_id"],
            time_dono_id=data["time_dono_id"],
            clube_id=data["clube_id"],
            nome=data["nome"],
            descricao=data["descricao"],
            slug=data["slug"],
            tipo=data["tipo"],
            tipo_flamula=data["tipo_flamula"],
            tipo_estampa_flamula=data["tipo_estampa_flamula"],
            tipo_adorno_flamula=data["tipo_adorno_flamula"],
            cor_primaria_estampa_flamula=data["cor_primaria_estampa_flamula"],
            cor_secundaria_estampa_flamula=data["cor_secundaria_estampa_flamula"],
            cor_borda_flamula=data["cor_borda_flamula"],
            cor_fundo_flamula=data["cor_fundo_flamula"],
            url_flamula_svg=data["url_flamula_svg"],
            url_flamula_png=data["url_flamula_png"],
            tipo_trofeu=data["tipo_trofeu"],
            cor_trofeu=data["cor_trofeu"],
            url_trofeu_svg=data["url_trofeu_svg"],
            url_trofeu_png=data["url_trofeu_png"],
            editorial=data["editorial"],
            patrocinador=data["patrocinador"],
            mata_mata=data["mata_mata"],
            inicio_rodada=data["inicio_rodada"],
            fim_rodada=data["fim_rodada"],
            quantidade_times=data["quantidade_times"],
            sorteada=data["sorteada"],
            mes_ranking_num=data["mes_ranking_num"],
            mes_variacao_num=data["mes_variacao_num"],
            camp_ranking_num=data["camp_ranking_num"],
            camp_variacao_num=data["camp_variacao_num"],
            imagem=data["imagem"],
            amigos=amigos,
            total_amigos_na_liga=data['total_amigos_na_liga'],
            total_times_liga=data['total_times_liga']
        )


class Amigo(object):

    def __init__(self, time_id, nome, nome_cartola, slug, facebook_id, url_escudo_png, url_escudo_svg,
                 url_escudo_placeholder_png, foto_perfil, assinante):
        self.time_id = time_id
        self.nome = nome
        self.nome_cartola = nome_cartola
        self.slug = slug
        self.facebook_id = facebook_id
        self.url_escudo_png = url_escudo_png
        self.url_escudo_svg = url_escudo_svg
        self.url_escudo_placeholder_png = url_escudo_placeholder_png
        self.foto_perfil = foto_perfil
        self.assinante = assinante

    def __str__(self):
        return "{time_id}={nome}".format(time_id=self.time_id, nome=self.nome)

    @classmethod
    def parse_json(cls, data):
        return cls(
            time_id=data["time_id"],
            nome=data["nome"],
            nome_cartola=data["nome_cartola"],
            slug=data["slug"],
            facebook_id=data["facebook_id"],
            url_escudo_png=data["url_escudo_png"],
            url_escudo_svg=data["url_escudo_svg"],
            url_escudo_placeholder_png=data["url_escudo_placeholder_png"],
            foto_perfil=data["foto_perfil"],
            assinante=data["assinante"]
        )
