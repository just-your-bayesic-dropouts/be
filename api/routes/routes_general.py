#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import logging

import requests
from flask import Blueprint, jsonify
from elasticsearch import Elasticsearch
from flask import request
from api.utils.auth import authenticate_jwt, generate_jwt, JWT
from api.utils.constants import notFound, permission, required, exists, invalid
from api.utils.index_data import index_data
from api.utils.index_ingest import ingest_data
from api.utils.responses import response_with
from api.utils import responses as resp

route_path_general = Blueprint("route_path_general", __name__)


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
d = ingest_data("/Users/benkrig/Downloads/1000.json")
index_data(d, es)


@route_path_general.route('/search', methods=['GET'])
def search():
    try:
        # get query
        q = request.args.get('q')
        logging.info(q)
        # request to elastic search
        r = es.search(index="test_index", size=20, body={
            "query": {
                "query_string": {
                    "default_field": "title",
                    "query": q
                }
            }
        })

        json_response = json.loads(json.dumps(r))

        return response_with(resp.SUCCESS_200, message=json_response)
    except Exception as e:
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)
