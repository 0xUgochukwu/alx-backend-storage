#!/usr/bin/env python3
'''
    NoSQL Databases
'''


def insert_school(mongo_collection, **kwargs):
    ''' Inserts into a collection '''
    return mongo_collection.insert(kwargs)
