import logging

from elasticsearch import Elasticsearch

from api.utils.index_ingest import ingest_data


def index_data(ingest, es):
    i = 0
    for d in ingest:
        if i == 100:
            break
        res = es.index(index="test_index", doc_type='product', id=i, body=d)
        logging.error(res['result'])
        i += 1
    es.indices.refresh(index="test_index")


if __name__ == "__main__":
    clean_data = ingest_data("/Users/benkrig/Downloads/1000.json")
