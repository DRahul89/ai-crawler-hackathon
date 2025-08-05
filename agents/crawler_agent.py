from agents.tools.scraper_tool import WebScraperTool
from agents.tools.pdf_tool import PDFTool

class CrawlerAgent:
    def __init__(self):
        self.scraper = WebScraperTool()
        self.pdf = PDFTool()

    def crawl_site(self, url):
        texts, pdfs = self.scraper.scrape(url)
        pdf_docs = []
        for link in pdfs:
            pdf_docs.extend(self.pdf.load_pdf(link))
        return texts + [doc.page_content for doc in pdf_docs]