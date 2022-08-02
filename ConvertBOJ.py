import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

from bs4 import BeautifulSoup
from urllib import request
from pathlib import Path

import os
import shutil
import time

cred = credentials.Certificate("blog-lr-b18ce-0de4250a02bf.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

postList = os.listdir("../Blog_LR_Data_Temp")

# Add Posting Layout on Each File
for post in postList:
    with open(f"../Blog_LR_Data_Temp/{post}/post.md") as f1:
        with open(f"../Blog_LR_Data_Temp/{post}/temp.md", "w") as f2:
            f2.write(f"[문제 바로가기](https://boj.kr/{post})\n")
            f2.write("\n")
            f2.write("```c++\n")
            for line in f1:
                f2.write(line)
            f2.write("```")

# Remove Temporaty Files
for post in postList:
    os.mkdir(f"../Blog_LR_Data_Temp/boj-{post}")
    with open(f"../Blog_LR_Data_Temp/{post}/temp.md") as f1:
        with open(f"../Blog_LR_Data_Temp/boj-{post}/post.md", "w") as f2:
            for line in f1:
                f2.write(line)

postList = os.listdir("../Blog_LR_Data/solving")
postList.sort()

# Upload Post Datas to Firebase
for post in postList:
    if post[0] == "b":
        problem = post.replace("boj-", "")
        print(problem)

        url = f"https://acmicpc.net/problem/{problem}"
        html = request.urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string.replace('번:', '. ')

        doc_ref = db.collection(u"solving").document(problem)
        doc_ref.set({
            u"isPinned": True,
            u"date": f"BOJ {problem}",
            u"tag": ["BOJ", "C++"],
            u"title": title,
            u"url": post,
        })8