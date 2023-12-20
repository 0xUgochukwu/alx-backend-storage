#!/usr/bin/env python3
'''
    NoSQL Databases
'''
from pymongo import MongoClient


if __name__ == '__main__':
    '''
        provides stats about nginx logs
    '''
    collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx

    print(f'{collection.count_documents()} logs')
    print('Methods:')

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"}
    )

    print(f'{status_check_count} status check')
