from langchain_postgres import PGVector
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import json

class VectorStoreTool:
    def __init__(self, collection_name: str, connection_string: str):
        self.collection_name = collection_name
        self.connection_string = connection_string

        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
       
        self.vector_store = PGVector(
            collection_name=self.collection_name,
            connection=self.connection_string,
            embeddings=self.embeddings,  
        )
    def save(self, docs):
        PGVector.from_documents(
            documents=docs,
            embedding=self.embeddings,
            collection_name=self.collection_name,
            connection=self.connection_string
        )
        

    def add_documents(self, documents: list[Document]):
        self.vector_store.add_documents(documents)

    def similarity_search(self, query: str, k: int = 4):
        return self.vector_store.similarity_search(query, k=k)
    
    def load(self):
        return PGVector(
            embeddings=self.embeddings,
            collection_name=self.collection_name,
            connection=self.connection_string,
        )
    def hash_state(self, hash):
        with open(f".meta_{self.collection_name}.json", "w") as f:
            json.dump({"hash": hash}, f)

    def get_last_hash(self):
        try:
            with open(f".meta_{self.collection_name}.json") as f:
                return json.load(f).get("hash")
        except:
            return None
