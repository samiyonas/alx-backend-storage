#!/usr/bin/env python3
""" return the list of school having a specific topic """


def schools_by_topics(mongo_collection, topic):
    """ return the list of school having a specific topic """
    docs = []

    for doc in mongo_collection.find():
        if topic in doc["topics"]:
            docs.append(doc)

    return docs
