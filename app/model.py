#把從資料庫保存下來的照片放入模型中進行預測
import torch
import numpy as np
import cv2
from pymongo import MongoClient
from gridfs import GridFS
from bson.objectid import ObjectId

def predict(input):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt',force_reload=True)
    cluster = MongoClient("mongodb://localhost:27017")
    db = cluster["react-fileupload-db"]
    col = db["fs.files"]
    fs = GridFS(db, collection="fs")
    query = {'_id': ObjectId(str(input))}

    for grid_out in fs.find(query):
        data = grid_out.read()  # 獲取圖片資料
        outf = open(str(input) + '.jpg', 'wb')  # 建立檔案
        outf.write(data)  # 儲存圖片
        outf.close()

    img = cv2.imread('/Users/yan/Desktop/model_api_h/'+input+'.jpg')
    results = str(model(img))
    return results[21]
