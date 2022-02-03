# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("codefor-fun-serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
