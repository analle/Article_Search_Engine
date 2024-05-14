import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# Function to read articles from CSV files
def read_articles(csv_file1, csv_file2):
    articles1 = pd.read_csv(csv_file1)["Article"]
    articles2 = pd.read_csv(csv_file2)["Article"]
    return articles1, articles2

def evaluate_articles(csv_file1, csv_file2):
    # Read articles from CSV files
    articles1, articles2 = read_articles(csv_file1, csv_file2)

    # Initialize counters
    total_true = len(articles1)  # Total number of true cases
    true_positives = 0  # Correctly identified articles
    predicted_positives = len(articles2)  # Total predictions made

    # Compare articles and update counters
    for article1, article2 in zip(articles1, articles2):
        if article1.strip() == article2.strip():
            true_positives += 1

    # Calculate precision, recall, and F1 score
    precision = true_positives / predicted_positives if predicted_positives else 0
    recall = true_positives / total_true if total_true else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0

    return precision, recall, f1




csv_file1 = r"predicted_articles.csv"
csv_file2 = r"testing_set.csv"
precision, recall, f1 = evaluate_articles(csv_file1, csv_file2)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
