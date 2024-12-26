import ollama
from httpx import stream
from pyexpat.errors import messages
import psycopg2
import json

# Initialize the Ollama chat model
model1 = ollama.chat(
    model="tinyllama",
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    stream=True,
)



def generate_vectors():
    conn, cur = init_connection()
    documents = [
        "Llamas are members of the camelid family meaning they're pretty closely related to vicuñas and camels",
        "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands",
        "Llamas can grow as much as 6 feet tall though the average llama between 5 feet 6 inches and 5 feet 9 inches tall",
        "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight",
        "Llamas are vegetarians and have very efficient digestive systems",
        "Llamas live to be about 20 years old, though some only live for 15 years and others live to be 30 years old",
    ]
    for i, d in enumerate(documents):
        response = ollama.embeddings(model="nomic-embed-text", prompt=d)
        embedding = response["embedding"]
        cur.execute(
            "INSERT INTO py_vector_store (content, metadata, embedding) VALUES (%s, %s, %s)",
            (d, json.dumps({"index_doc": i}), embedding,),
        )
    conn.commit()
    cur.close()
    conn.close()
    print("Vectors generated")


def init_connection():
    conn = psycopg2.connect(database="vector", user="user", password="pass", host="localhost",port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""
        CREATE EXTENSION IF NOT EXISTS vector;
        CREATE EXTENSION IF NOT EXISTS hstore;
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
        
        CREATE TABLE IF NOT EXISTS py_vector_store (
            id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
            content text,
            metadata json,
            embedding vector(768)  --1536 is the default embedding dimension
        );
        
        CREATE INDEX ON py_vector_store USING HNSW (embedding vector_cosine_ops);
    """)
    print("Connection established")
    return conn, cur

def search_vectors(query):
    conn, cur = init_connection()
    response = ollama.embeddings(model="nomic-embed-text", prompt=query)
    embedding = response["embedding"]
    cur.execute(
        "SELECT content, metadata FROM py_vector_store ORDER BY embedding <-> %s::vector",
        (embedding,),
    )
    results = cur.fetchall()
    print("Results:" + str(results))
    cur.close()
    conn.close()
    return results

def chat_with_model(user_input):
    results = search_vectors(user_input) #tuple list of (content, metadata)
    if len(results) == 0:
        print("I'm sorry, I don't know the answer to that question.")
        return
    list = [x for x, y in results]

    prompt = """
    Question: {}
    Use the following information to answer your question:
    {}""".format(user_input, list)

    model1 = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    for chunk in model1:
        print(chunk["message"]["content"], end="", flush=True)




if __name__ == "__main__":
    # user_input = "Hello, how are you?"
    # chat_with_model(user_input)
    generate_vectors()
    chat_with_model("Tell me about llamas, short please")
