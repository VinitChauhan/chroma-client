
import chromadb
from chromadb import PersistentClient
from embadding_generator import generate_embedding
from sample_data import generate_student_records  

db_path = "../chroma-db"

def chroma_client():
    client = chromadb.PersistentClient(path=db_path)
    return client

def get_all_collections():
    collections = chroma_client().list_collections()
    print("Collections in DB:", collections)
    return collections

def create_new_collection(collection_name):
    client = chroma_client()
    collections = client.list_collections()
    if not any(col.name == collection_name for col in collections):
        collection = client.create_collection(name=collection_name)
        print(f"Collection '{collection_name}' created.")
        return collection
    else:
        print(f"Collection '{collection_name}' already exists.")
        return client.get_collection(name=collection_name)
 
class Document:
    def __init__(self, document_id, document_data):
        self.id = document_id
        self.data = document_data

def add_document_to_collection(collection, doc: Document):
    embadding = generate_embedding(doc.data)
    if embadding is None:
        print(f"Failed to generate embedding for document {doc.id}.")
        return

    collection.add(
        ids=[doc.id],
        documents=[doc.data],
        metadatas=[{"source": "dev"}],
        embeddings=[embadding] 
    )

if __name__ == "__main__":
    get_all_collections()
    collection_name = "sample_collection"
    collection = create_new_collection(collection_name=collection_name)
    # sample_doc = Document(document_id="doc1", document_data="This is a sample document.")

    for record in generate_student_records(num_students=5):
        doc = Document(document_id=record['student_id'], document_data=str(record))
        add_document_to_collection(collection, doc=doc)

    documents = collection.get()
    # all_documents is typically a dict with keys like 'ids', 'documents', 'metadatas', etc.
    for doc_id, doc_data in zip(documents.get('ids', []), documents.get('documents', [])):
        print(f"Document ID: {doc_id}, Data: {doc_data}")

    # print("Retrieved Documents:", all_documents)
