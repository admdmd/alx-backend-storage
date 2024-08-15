#!/usr/bin/env python3
""" Lists * documents in Python
"""

import pymongo


def list_all(mongo_collection):
    """ list_all.
    """
    docs = mongo_collection.find()
    return [x for x in docs]
