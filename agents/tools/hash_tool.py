import hashlib

class HashTool:
    def content_hash(self, text):
        return hashlib.md5(text.encode()).hexdigest()