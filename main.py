from agents.crawler_agent import CrawlerAgent
from agents.embedder_agent import EmbedderAgent
from agents.answer_agent import AnswerAgent
from urllib.parse import urlparse

def get_collection_name(url):
    return urlparse(url).netloc.replace(".", "_")

def main():
    url = "https://amintiri.in/collections/celebration-cakes"
    collection = get_collection_name(url)
    print("test "+ collection)
    connection_string = "postgresql+psycopg2://myuser:mypassword@localhost:5432/langchain_db"

    # 1. Crawl site
    print("🔍 Crawling site...")
    crawler = CrawlerAgent()
    all_content = crawler.crawl_site(url)

    # 2. Embed if changed
    embedder = EmbedderAgent(collection, connection_string)
    embedder.embed_if_needed(all_content)

    # 3. Ask a question
    question = input("\n💬 Your question: ")
    answer_agent = AnswerAgent(collection, connection_string)
    print("\n📘 Answer:\n")
    print(answer_agent.answer(question))

if __name__ == "__main__":
    main()
