from agents.tools.hash_tool import HashTool
from agents.tools.embed_tool import EmbedTool
from agents.tools.vector_tool import VectorStoreTool

class EmbedderAgent:
    def __init__(self, collection_name, connection_string):
        self.hasher = HashTool()
        self.splitter = EmbedTool()
        self.vector = VectorStoreTool(collection_name, connection_string)

    def embed_if_needed(self, all_texts):
        full_text = "\n\n".join(all_texts)
        new_hash = self.hasher.content_hash(full_text)
        last_hash = self.vector.get_last_hash()

       

        docs = self.splitter.split_texts([full_text])
        self.vector.save(docs)
        self.vector.hash_state(new_hash)
        print("✅ Vector DB updated.")
        return True
