import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
from utils import clean_text,load_config
import gradio as gr
import pickle


class ArticleSearchEngine:
    def __init__(self, model_path, data_path):
        # Load model
        self.model = SentenceTransformer(model_path)
        
        # Load data
        self.data = pd.read_csv(data_path, encoding='latin-1')

        # Initialize index
        self.initialize_index()

    
    def initialize_index(self):
        """
        Initialize the Faiss index using Sentence Transformer embeddings.
        """

        ##commenting this code which generates the article embedding for faster loading 
        
        # Encode article text
        #self.data['merged'] = self.data.apply(lambda row: f"{row['Heading']}. {row['Article']}", axis=1)
        
        #article_texts = [clean_text(text) for text in self.data['merged'].tolist()]
        #article_embeddings = self.model.encode(article_texts)
        ## Save encoded embeddings to cache
        #file_path=r"C:\Users\AnalleJ\Desktop\Anya\article_embeddings.pkl"
        #with open(file_path, "wb") as f:
        #   pickle.dump(article_embeddings, f)
    

        file_path=r"article_embeddings.pkl"
        with open(file_path, "rb") as f:
            article_embeddings = pickle.load(f)
    
        
        # Initialize and add embeddings to the index
        self.index = faiss.IndexFlatIP(article_embeddings.shape[1])
        self.index.add(article_embeddings)
        return

    def search_articles(self, query, start_date=None, end_date=None, news_type=None):
        """
        Search for articles based on the query.
        
        Args:
        - query (str): The search query.
        
        Returns:
        - heading (str): Heading of the most relevant article.
        - article (str): Content of the most relevant article.
        """

        # Encode the query
        query_embedding = self.model.encode([query])[0]

        # Perform approximate nearest neighbor search
        _, indices = self.index.search(query_embedding.reshape(1, -1), k=len(self.data))
        # Filter articles based on additional criteria
        filtered_indices = list(range(len(self.data)))
        # Return the most relevant article
        for idx in indices[0]:
            if idx in filtered_indices:
                return self.data.loc[idx, 'Heading'], self.data.loc[idx, 'Article']



# Load configuration
config = load_config(r"config.yaml")

# Extract model, index, and data paths from config
model_path = config["sentence_embedding"]
data_path = config["data_path"]

# Create an object from the ArticleSearchEngine class
search_engine = ArticleSearchEngine(model_path, data_path)

def search_articles(query):
    heading, article = search_engine.search_articles(query)
    return heading, article

# Create Gradio interface
gr.Interface(
    fn=search_articles,
    inputs=gr.Textbox(lines=2, label="Enter search query"),
    outputs=["text", "text"],
    title="Article Search Engine",
    description="Enter a query to search for relevant articles",
).launch(share=True, debug=True)