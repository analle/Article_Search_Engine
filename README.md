# Article_Search_Engine

## Article Search Engine Prototype

This project addresses the problem of finding relevant articles based on user queries.

### Overview

This repository contains various files that outline my approach to solving the problem.

### Setup

To begin, make sure to install the required libraries by running the `requirements.txt` file.

### Data Analysis

I started by performing preliminary data analysis to gain insights into the dataset. The `analysis.py` file contains this analysis, which can be run separately to get valuable insights.

### Preprocessing

I applied the preprocessing steps using function clean_text in utils.py

### Building the Prototype

The first step in building the prototype was to convert text into vectors. For this purpose, I utilized the Sentence Transformer model, specifically designed for semantic search.

To find the closest articles to a given query, I employed the Faiss library, known for its efficiency in similarity search.

For creating a user-friendly interface, I utilized Gradio, which allows for easy interaction with the prototype. Upon running the code, clicking the provided link launches the prototype.

To run the prototype, execute the `search_query.py` file as the main script. 

**Note:** Article embeddings have been saved in a pickled file to expedite loading time. Loading the embeddings typically takes around 4 minutes.
### Evaluation

In the absence of a testing set, I thought of using ChatGPT to generate test queries. The `generate-test.py` file contains the code for generating relevant queries and evaluating if the expected articles are retrieved.

To assess the performance of the prototype, I calculated precision, recall, and F1 score using the `evaluate.py` script.

### Conclusion

It's important to note that there are numerous avenues for further exploration and improvement to enhance the prototype's results.
