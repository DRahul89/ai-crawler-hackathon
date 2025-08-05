import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebScraperTool:
    def scrape(self, root_url, max_links=25):
        visited = set()
        to_visit = [root_url]
        all_text = []
        pdf_links = []

        while to_visit and len(visited) < max_links:
            url = to_visit.pop()
            if url in visited: continue
            visited.add(url)

            try:
                res = requests.get(url, timeout=10)
                soup = BeautifulSoup(res.text, "html.parser")
                all_text.append(soup.get_text(separator="\n", strip=True))

                for link in soup.find_all("a", href=True):
                    full = urljoin(url, link["href"])
                    if full.endswith(".pdf"):
                        pdf_links.append(full)
                    elif full.startswith(root_url):
                        to_visit.append(full)
            except:
                continue

        return all_text, pdf_links
