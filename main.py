import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("blog-lr-b18ce-751915feeb1a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

dataFile = open("Blog_DB.json", "r")
dataJson = json.load(dataFile)
dataFile.close()

num = 1
for dataItem in dataJson:
    doc_ref = db.collection(u"blog").document(str(num).zfill(5))
    doc_ref.set({
        u"isPinned": dataItem["pinned"],
        u"date": dataItem["postDate"],
        u"tag": dataItem["postTag"],
        u"title": dataItem["postTitle"],
        u"url": dataItem["postURL"],
    })
    num += 1

dataFile = open("Project_DB.json", "r")
dataJson = json.load(dataFile)
dataFile.close()

num = 1
for dataItem in dataJson:
    doc_ref = db.collection(u"project").document(str(num).zfill(5))
    doc_ref.set({
        u"isPinned": dataItem["pinned"],
        u"date": dataItem["postDate"],
        u"tag": dataItem["postTag"],
        u"title": dataItem["postTitle"],
        u"url": dataItem["postURL"],
    })
    num += 1

dataFile = open("Solving_DB.json", "r")
dataJson = json.load(dataFile)
dataFile.close()

num = 1
for dataItem in dataJson:
    doc_ref = db.collection(u"solving").document(str(num).zfill(5))
    doc_ref.set({
        u"isPinned": dataItem["pinned"],
        u"date": dataItem["postDate"],
        u"tag": dataItem["postTag"],
        u"title": dataItem["postTitle"],
        u"url": dataItem["postURL"],
    })
    num += 1