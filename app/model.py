# -*- coding: UTF-8 -*-
import numpy as np
import globals
from pymongo import MongoClient
from gridfs import GridFS

globals.results=' '
globals.count=0

def predict(input):
    cluster = MongoClient("mongodb+srv://yan31:yan31@cluster0.xfxba5r.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["ootdData"]
    col = db["fs.files"]
    gridFS = GridFS(db, collection="fs")
    query = {"filename": input}
    mydoc = col.find(query)

    for x in mydoc:
        tag1 = x['tag1']
        tag2 = x['tag2']

    return str(tag1),str(tag2)
