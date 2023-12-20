#!/usr/bin/env python3
'''
    NoSQL Databases
'''


def update_topics(mongo_collection, name, topics):
    '''
         Changes all topics  of a school document
         based on a name.
    '''
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}})
