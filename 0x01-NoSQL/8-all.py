#!/usr/bin/env python3
'''
    NoSQL Databases
'''

def list_all(mongo_collection):
    '''
        lists all documents in a mongo collection 
    '''
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents

