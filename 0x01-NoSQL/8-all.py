#!/usr/bin/env python3
""" List all documents in a collection """


def list_all(mongo_collection):
    """ List all documents in a collection """
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
