# encoding: utf-8
import json
from cartolafc.errors import CartolaFCError


def convert_json_to_data(json_data):
    try:
        data = json.loads(json_data)
        if 'mensagem' in data and data['mensagem']:
            raise CartolaFCError(data['mensagem'].encode('utf-8'))
        return data
    except ValueError as error:
        raise CartolaFCError('Globo.com - Desculpe-nos, nossos servidores estão sobrecarregados.')