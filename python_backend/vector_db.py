import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

class VectorDB:
    def __init__(self):
        self.index = None
        self.texts = []
        self.data_embeddings = []
        
    def create_index(self, embedding_dim):
        self.index = faiss.IndexFlatL2(embedding_dim)
    
    def add_data(self, texts):
        self.texts.extend(texts)
        for text in texts:
            embedding = model.encode(text)
            self.data_embeddings.append(embedding)
        self.index.add(np.array(self.data_embeddings).astype('float32'))

    def query(self, query, k=5):
        query_embedding = model.encode(query)
        D, I = self.index.search(np.array([query_embedding]).astype('float32'), k)
        return [self.texts[i] for i in I[0]]