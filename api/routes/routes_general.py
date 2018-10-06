#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import logging

import requests
from flask import Blueprint
from elasticsearch import Elasticsearch
from flask import request
from api.utils.auth import authenticate_jwt, generate_jwt, JWT
from api.utils.constants import notFound, permission, required, exists, invalid
from api.utils.responses import response_with
from api.utils import responses as resp

route_path_general = Blueprint("route_path_general", __name__)


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


@route_path_general.route('/search', methods=['GET'])
def get_json():
    try:
        # get query
        q = request.args.get('q')

        # request to elastic search
        r = requests.get('http://localhost:9200/{}'.format(q))

        json_response = r.content.decode('utf8').replace("'", '"')

        return response_with(resp.SUCCESS_200, message=json_response)
    except Exception as e:
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)
