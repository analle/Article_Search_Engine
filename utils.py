import re
import pandas as pd
import string
from nltk.corpus import stopwords
import nltk 
nltk.download('stopwords')
import yaml

def clean_text(text):
    """
    Preprocess the text by following some cleaning steps.
    
    Args:
        text (str): The input text to be cleaned.
    
    Returns:
        str: The cleaned text.
    """
    # Remove these special characters
    characters_to_remove = '[/(){}[]|@,;]:>'

    # Remove stopwords
    #STOPWORDS = set(stopwords.words('english'))
    
    # Convert text to lower case
    #text = text.lower()
    
    # Remove special characters
    text = re.sub('[' + re.escape(characters_to_remove) + ']', ' ', text)
    
    # Remove stopwords and punctuation
    cleaned_text = ' '.join(word for word in text.split() if word not in string.punctuation)
    
    return cleaned_text.strip()



def load_config(config_path: str) -> dict:
    """
    Load configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Configuration parameters loaded from the file.
    """
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

# Example usage:
# index_path = "path_to_faiss_index"
# index = read_index(index_path)



data = pd.read_csv(r'C:\Users\AnalleJ\Desktop\ayna\Articles.csv',encoding='latin-1')
# Preprocess articles
data['processed_article'] = data['Article'].apply(clean_text)