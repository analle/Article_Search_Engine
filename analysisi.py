import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def basic_statistics(data):
    """
    Perform basic statistical analysis on the dataset.
    
    Args:
        data (pd.DataFrame): The input data containing articles.
    
    Returns:
        None
    """

    # Conduct Some Basic Statistics
    print("\n\033[1mMissing Values:\033[0m")
    print(data.isnull().sum())
    # Since no missing values, no need to delete any

    #check how many unique category in the data
    print("\n\033[1mArticle Count by News Type:\033[0m")
    print(data["NewsType"].value_counts())

    print("\n\033[1mArticle Count by Date:\033[0m")
    print(data["Date"].value_counts().sort_index())

def word_count_analysis(data):
    """
    Perform word count analysis on the dataset.
    
    Args:
        data (pd.DataFrame): The input data containing articles.
    
    Returns:
        None
    """
    
    # Calculate lengths of each article by words
    data['WordCount'] = data['Article'].apply(lambda x: len(str(x).split()))
    unique_words = set(" ".join(data['Article']).split())
    num_unique_words = len(unique_words)

    # Calculate shortest, longest, and average length
    shortest_length = data['WordCount'].min()
    longest_length = data['WordCount'].max()
    average_length = data['WordCount'].mean()

    print("Number of unique words:", "\033[1m", num_unique_words, "\033[0m")
    print("Shortest Article Length by word:", "\033[1m", shortest_length, "\033[0m")
    print("Longest Article Length by word:", "\033[1m", longest_length, "\033[0m")
    print("Average Article Length by word:", "\033[1m", average_length, "\033[0m")

    # Calculate word counts for each category
    business_word_counts = data.loc[data['NewsType'] == 'business', 'WordCount']
    sports_word_counts = data.loc[data['NewsType'] == 'sports', 'WordCount']

    # Plot counts for each category
    plt.figure(figsize=(8, 4))
    sns.histplot(business_word_counts, bins=range(0, max(data['WordCount']) + 1, 10), color='blue', alpha=0.5, label='Business')
    sns.histplot(sports_word_counts, bins=range(0, max(data['WordCount']) + 1, 10), color='orange', alpha=0.5, label='Sports')
    plt.xlabel("Number of words")
    plt.ylabel("Count")
    plt.title("Length of Business and Sports Articles")
    plt.legend()
    plt.show()

    # Calculate how many articles have more than 1000 words, this is done after the observation noticed from the plot
    articles_above_1000_words = data[data['WordCount'] > 1000]
    num_articles_above_1000_words = len(articles_above_1000_words)

    print("Number of articles with more than 1000 words:", "\033[1m", num_articles_above_1000_words, "\033[0m")

#Example usage:
data = pd.read_csv(r'Articles.csv',encoding='latin-1')
basic_statistics(data)
word_count_analysis(data)
