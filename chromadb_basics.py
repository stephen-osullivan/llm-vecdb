"""
demonstrates the basics of a chromadb vector database
the distnace between between the query and the items in the collection is calculated and
the documents with the smallest distances, along with their sources are returned.
The distances are calculated using an mini LM embedding (all-MiniLM-L6-v2).
Notice how it detects "felines" as being closer in meaning to "cat" than elephant.

"""

import chromadb

chroma_client = chromadb.Client()

# create vector db called "my_collection"
collection = chroma_client.create_collection(name = "my_collection")

collection.add(
    documents = ["cats have whiskers", "elephants have trunks"],
    metadatas= [{"source": 'cat wiki'}, {"source": "elephant wiki"}], # 1 per do document
    ids = ["id1", "id2"] # 1 per document
)

results = collection.query(
    query_texts = ["what do felines have?"],
    n_results=2
)

print(results)