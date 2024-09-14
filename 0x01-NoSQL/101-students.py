#!/usr/bin/env python3
""" returns all students sorted by average score """


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    for doc in mongo_collection.find():
        summation = 0
        for i in doc["topics"]:
            summation += i["score"]
        mongo_collection.update_one(
                doc, {"$set": {"averageScore": summation/3}}
                )

    documents = mongo_collection.find().sort('averageScore', -1)

    return documents
