import requests
import os
from langchain.document_loaders import PyPDFLoader

class PDFTool:
    def __init__(self, storage_path="pdfs"):
        os.makedirs(storage_path, exist_ok=True)
        self.path = storage_path

    def load_pdf(self, url):
        filename = os.path.join(self.path, url.split("/")[-1])
        res = requests.get(url)
        with open(filename, "wb") as f:
            f.write(res.content)
        return PyPDFLoader(filename).load()