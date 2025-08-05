1.install docker file
2.docker pull ankane/pgvector
3.run this command 

4.docker run -e POSTGRES_USER=myuser \
           -e POSTGRES_PASSWORD=mypassword \
           -e POSTGRES_DB=langchain_db \
           --name my_postgres \
           -p 5432:5432 \
           -d ankane/pgvector
5.install python3.10 
6.create virtual environment python3.10  -m venv .venv
7.activate it source .venv/bin/activate
8.now install all below dependencies
    pip install langchain openai beautifulsoup4 requests faiss-cpu PyMuPDF