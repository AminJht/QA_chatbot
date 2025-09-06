import chromadb
from transformers import AutoTokenizer, AutoModel
import torch

client = chromadb.PersistentClient(path="./chroma_db")
model_name= "myrkur/sentence-transformer-parsbert-fa-2.0"

class search_db:
    def __init__(self):
  
        self.collection= client.get_collection(name="text_chunks")

        self.hf_tokenizer= AutoTokenizer.from_pretrained(model_name, cache_dir="local_models")
        self.hf_model = AutoModel.from_pretrained(model_name, cache_dir="local_models")

    def get_embedding(self, chunk):
        # تبدیل chunk به توکن‌ها
        inputs = self.hf_tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=512)
        # غیرفعال کردن گرادیان برای سرعت
        with torch.no_grad():
            # گرفتن خروجی مدل
            outputs = self.hf_model(**inputs)
        # میانگین‌گیری برای تولید embedding سطح chunk
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy().tolist()
        return embedding
    def search(self, text:str):

        input_norm = self.get_embedding(text)

        results_db= self.collection.query(
            query_embeddings=[input_norm],
            n_results=5,
        )
        filtered_dict = {}
        max_distance=0.4
        for i in range(len(results_db['ids'][0])):
            distance = results_db['distances'][0][i]
            
            if distance < max_distance:
                doc_id = results_db['ids'][0][i]
                
                filtered_dict[doc_id] = {
                    'document': results_db['documents'][0][i],
                    'distance': distance,
                }
            return filtered_dict 
