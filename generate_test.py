import openai
import pandas as pd
import csv

openai.api_key = "include api key"

def call_openai_gpt4(text):
    """
    Function to send a single request to the OpenAI GPT-4 model.
    """

    response = openai.ChatCompletion.create(
    model= "gpt-4-turbo",
    messages= [{ "role": "system" , "content": "You are a model that extract a suitable query that suits a given article.\n You will be given an article, return a relevant search query from a user and an irrelevant one.\n Return the response as relevant:\n irrelevant:" },
            {"role": "user", "content": "this is the article:{}".format(text)}],
    )
    # import pdb;pdb.set_trace()
    # Extract relevant and irrelevant queries from the response
    relevant_query = response.choices[0].message.content.split("\n")[0].replace("relevant:", "").strip()
    irrelevant_query = response.choices[0].message.content.split("\n")[1].replace("irrelevant:", "").strip()
    
    # Save the input article and the extracted queries to an Excel file
    
    # Append the new article and queries to the existing CSV file or create a new one if it doesn't exist
    with open(r"testing_set.csv", "a", newline="",encoding="utf-8") as csvfile:
        # Add the column headers if the file is empty
        
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(["Article", "Relevant Query", "Irrelevant Query"])
        writer.writerow([text, relevant_query, irrelevant_query])
def process_file(line):
    """
    Reads sentences from a file and calls the OpenAI API for each sentence.
    """
    
    response_text = call_openai_gpt4(line.strip())
    print("Input:", line)
    print("Response:", response_text)
    
    print("-" * 40)

# Load dataset
data = pd.read_csv(r"Articles.csv",encoding='latin-1')
da=data['Article']
for i in da[:100]:
  process_file(i)







