import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("blog-lr-b18ce-0de4250a02bf.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

dataFile = open("Blog_DB.json", "r")
dataJson = json.load(dataFile)
dataFile.close()

dataList = []
for dataItem in dataJson:
    dataList.append({
        u"isPinned": dataItem["pinned"],
        u"date": dataItem["postDate"],
        u"tag": dataItem["postTag"],
        u"title": dataItem["postTitle"],
        u"url": dataItem["postURL"],
    })

dataList.reverse()

num = 1
for dataItem in dataList:
    doc_ref = db.collection(u"blog").document(str(num).zfill(5))
    doc_ref.set({
        u"isPinned": dataItem["isPinned"],
        u"date": dataItem["date"],
        u"tag": dataItem["tag"],
        u"title": dataItem["title"],
        u"url": dataItem["url"],
    })
    num += 1

dataFile = open("Project_DB.json", "r")
dataJson = json.load(dataFile)
dataFile.close()

dataList = []
for dataItem in dataJson:
    dataList.append({
        u"isPinned": dataItem["pinned"],
        u"date": dataItem["postDate"],
        u"tag": dataItem["postTag"],
        u"title": dataItem["postTitle"],
        u"url": dataItem["postURL"],
    })

dataList.reverse()

num = 1
for dataItem in dataList:
    doc_ref = db.collection(u"project").document(str(num).zfill(5))
    doc_ref.set({
        u"isPinned": dataItem["isPinned"],
        u"date": dataItem["date"],
        u"tag": dataItem["tag"],
        u"title": dataItem["title"],
        u"url": dataItem["url"],
    })
    num += 1

dataFile = open("Solving_DB.json", "r")
dataJson = json.load(dataFile)
dataFile.close()

dataList = []
for dataItem in dataJson:
    dataList.append({
        u"isPinned": dataItem["pinned"],
        u"date": dataItem["postDate"],
        u"tag": dataItem["postTag"],
        u"title": dataItem["postTitle"],
        u"url": dataItem["postURL"],
    })

dataList.reverse()

num = 1
for dataItem in dataList:
    doc_ref = db.collection(u"solving").document(str(num).zfill(5))
    doc_ref.set({
        u"isPinned": dataItem["isPinned"],
        u"date": dataItem["date"],
        u"tag": dataItem["tag"],
        u"title": dataItem["title"],
        u"url": dataItem["url"],
    })
    num += 1