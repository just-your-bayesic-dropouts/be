import json


def ingest_data(fn):
    """Takes a .json and returns an ingested, sanitized form of output
    :param fn: String
    :return: [ { Index } ]
    """
    dirty_data = []
    clean_data = []

    with open(fn) as f:
        dirty_data = f.readlines()

    clean_data = [json.loads(line) for line in dirty_data]

    return clean_data

    print('success')


if __name__ == "__main__":
    ingest_data("/Users/benkrig/Downloads/1000.json")
