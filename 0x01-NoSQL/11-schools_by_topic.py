#!/usr/bin/env python3
'''
    NoSQL Databases
'''


def schools_by_topic(mongo_collection, topic):
    ''' list of schools having a specific topic '''
    return list(mongo_collection.find({"topics": topic}))
