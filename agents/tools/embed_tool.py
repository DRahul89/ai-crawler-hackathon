from langchain.text_splitter import RecursiveCharacterTextSplitter

class EmbedTool:
    def split_texts(self, texts):
        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
        return splitter.create_documents(texts)