#!/usr/bin/env python3
""" provide some stats about Nginx logs """


def nginx_stats(collection):
    """ provide some stats about Nginx logs """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(collection.count_documents({})))
    
    for i in methods:
        print('\tmethod {}: {}'.format(i, collection.count_documents({"method": i})))

    print("{} status check".format(collection.count_documents({"method": "GET"}, {"path": "/status"})))

def main():
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    collection = db.collection

    nginx_stats(collection)

if __name__ == "__main__":
    main()
