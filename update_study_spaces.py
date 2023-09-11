import firebase_admin
from firebase_admin import credentials, firestore
from webscraper import get_study_spaces

# Initialize Firebase
cred = credentials.Certificate("my-file.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def store_study_spaces_in_firestore(spaces):
    for space in spaces:
        doc_ref = db.collection('study_spaces').document(space['title'])
        doc_ref.set(space)

def main():
    spaces = get_study_spaces()
    store_study_spaces_in_firestore(spaces)
    print("Study spaces updated successfully!")

if __name__ == "__main__":
    main()
