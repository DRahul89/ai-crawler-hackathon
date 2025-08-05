from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

class VectorSearchTool:
    def __init__(self, db_path):
        self.db = FAISS.load_local(db_path, OpenAIEmbeddings())

    def search(self, query, k=3):
        return self.db.similarity_search(query, k=k)
