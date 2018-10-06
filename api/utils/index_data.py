from elasticsearch import Elasticsearch



def index_data(ingest, es):
    i = 0
    for d in ingest:
        res = es.index(index="test_index", doc_type='product', id=i, body=d)
        print(res['result'])
        i += 1
    es.indices.resfresh(index="test_index")