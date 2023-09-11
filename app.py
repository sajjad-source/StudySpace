from flask import Flask, jsonify
from flask_cors import CORS
from webscraper import get_study_spaces  

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("my-file.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__, static_url_path='')
CORS(app)

def store_study_spaces_in_firestore(spaces):
    for space in spaces:
        doc_ref = db.collection('study_spaces').document(space['title'])
        doc_ref.set(space)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/spaces', methods=['GET'])
def api_spaces():
    spaces = get_study_spaces()
    store_study_spaces_in_firestore(spaces)
    return jsonify({'spaces': spaces})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
