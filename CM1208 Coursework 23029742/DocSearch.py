import re
import numpy as np
import math

def read_docs(file_path):
    with open(file_path, 'r') as file:
        return [re.sub(r'[^a-z\s]', '', line.strip().lower()) for line in file]

def build_dictionary(docs):
    dictionary = set()
    for doc in docs:
        dictionary.update(doc.split())
    return sorted(dictionary)

def build_inverted_index(docs, dictionary):
    inverted_index = {word: set() for word in dictionary}
    for i, doc in enumerate(docs, start=1):  # Start document IDs from 1
        for word in doc.split():
            inverted_index[word].add(i)
    return inverted_index

def search_documents(query, dictionary, inverted_index, docs):
    query_words = query.strip().lower().split()
    query_words = [word for word in query_words if word in dictionary]
    
    if not query_words:
        return set(), [0] * len(dictionary), [0] * len(docs)
    
    relevant_docs = set.intersection(*[inverted_index[word] for word in query_words])
    
    query_vector = [1 if word in query_words else 0 for word in dictionary]
    doc_vectors = []
    for i, doc in enumerate(docs, start=1):  # Start document IDs from 1
        doc_vector = [doc.split().count(word) for word in dictionary]
        doc_vectors.append(doc_vector)
    
    return relevant_docs, query_vector, doc_vectors

def vector_angle(v1, v2):
    dot_product = np.dot(v1, v2)
    magnitudes = np.linalg.norm(v1) * np.linalg.norm(v2)
    if magnitudes == 0:
        return 0
    cos_angle = dot_product / magnitudes
    angle_radians = np.arccos(np.clip(cos_angle, -1.0, 1.0))
    return math.degrees(angle_radians)

def main():
    docs = read_docs('docs.txt')
    dictionary = build_dictionary(docs)
    inverted_index = build_inverted_index(docs, dictionary)
    
    print(f"Words in dictionary: {len(dictionary)}\n")
    
    with open('queries.txt', 'r') as file:
        queries = [line.strip() for line in file]
    
    for query in queries:
        print(f"Query: {query}")
        relevant_docs, query_vector, doc_vectors = search_documents(query, dictionary, inverted_index, docs)
        
        if not relevant_docs:
            print("Relevant documents: None\n")
        else:
            print(f"Relevant documents: {' '.join(str(doc_id) for doc_id in relevant_docs)}")
            
            doc_angles = []
            for doc_id in relevant_docs:
                doc_vector = doc_vectors[doc_id - 1]  # Adjust index to start from 0
                angle = vector_angle(query_vector, doc_vector)
                doc_angles.append((doc_id, angle))
            
            doc_angles.sort(key=lambda x: x[1])
            for doc_id, angle in doc_angles:
                print(f"{doc_id} {angle:.5f}")
            
            print()

if __name__ == '__main__':
    main()