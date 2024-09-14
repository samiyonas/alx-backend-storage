#!/usr/bin/env python3
""" provide some stats about Nginx logs """


def nginx_stats(co):
    """ provide some stats about Nginx logs """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(co.count_documents({})))

    for i in methods:
        print(
            '\tmethod {}: {}'.format(
                i, co.count_documents({"method": i})
            )
        )
    print(
        '{} status check'.format(
            co.count_documents({"method": "GET", "path": "/status"})
        )
    )


def main():
    """ the main function where we setup the configuration """
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    collection = db.collection

    nginx_stats(collection)


if __name__ == "__main__":
    """ if this file is being run call the main function """
    main()
