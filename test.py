import csv
import json
# importing module
import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Create and configure logger
logging.basicConfig(filename="C:\python\python3.10v\CFF\Test.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.debug("Harmless debug Message")

# ---- File Conversion --------------------------------------------------------

def make_json(csvFile, jsonFile):
    log.debug("In make_json")
    log.debug(f'Converting {csvFile} to {jsonFile}')

    data = {}

    with open(csvFile, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)  # Open a csv reader

        # Convert each row into a dictionary, and add it to data
        count = 0
        for rows in csvReader:
            count = count+1
            address = {
                'City': rows['Address city'],
                'Street': rows['address street'],
                'Zipcode': rows['address zipcode']
            }
            student = {
                'Name': rows['SName'],
                'Gender': rows['SGender'],
                'DOB': rows['SDOB']
            }
            info = {
                'Name': rows['Name'],
                'Email': rows['Email'],
                'phonenumber': rows['phonenumber'],
                'Address': address,
                'Student' : student
            }
            data[count]= info
    # Open a json writer, and use the json.dumps()
    with open(jsonFile, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    print(f'converted CSV to JSON successfully')
    return jsonf;

def main():
    log.debug("In main")
    input_file = 'C:\python\python3.10v\CFF\Test.csv'
    json_file = 'C:\python\python3.10v\CFF\Test.json'
    jsonf=make_json(input_file, json_file)
    cred = credentials.Certificate("C:\python\python3.10v\CFF\codefor-fun-serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
#push the JSON data in firestore DB
    db = firestore.client()
    with open(json_file,'r') as jf:
        data = json.load(jf)
        db_ref = db.collection(u'users').document(u'userid').set(data)
#Query DB
    doc_ref = db.collection(u'users').document(u'userid')
    doc = doc_ref.get()
    if doc.exists:
     print(f'Users Data: {doc.to_dict()}')
    else:
     print(u'No such document!')
main()