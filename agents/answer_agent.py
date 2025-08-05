import os
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.tools.vector_tool import VectorStoreTool


class AnswerAgent:
    def __init__(self, collection_name, connection_string):
        self.vector = VectorStoreTool(collection_name, connection_string)

        # Chat model
        self.llm = ChatOpenAI(
            temperature=0.2,
            model="gpt-3.5-turbo",  # or "gpt-4"
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

        # Optional: Custom prompt
        self.prompt = PromptTemplate.from_template(
            """You are an intelligent assistant. Answer the user's question using only the provided context.

Context: {context}

Question: {question}

Answer:"""
        )

        # Lazy-loaded QA chain
        self.qa_chain = None

    def answer(self, query):
        # Load vector store
        store = self.vector.load()
        retriever = store.as_retriever()

        if not self.qa_chain:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                retriever=retriever,
                chain_type_kwargs={"prompt": self.prompt},
                return_source_documents=False
            )

        # Run query through LLM with retrieved context
        result = self.qa_chain.run(query)
        return result
