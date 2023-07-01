import requests
from bs4 import BeautifulSoup
import re

def search_web(topic):
    # Perform a web search using the topic
    search_url = f'https://www.google.com/search?q={topic}'  # Use Google as the search engine
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}  # Add appropriate headers to mimic a browser request
    response = requests.get(search_url, headers=headers)
    print("***********************************this is response",response)
    if response.status_code == 200:
        # Extract relevant information from the search results
        soup = BeautifulSoup(response.content, 'html.parser')
        search_results = soup.find_all('div', class_='yuRUbf')
        return [result.get_text() for result in search_results]
    else:
        return []


# Additional helper functions for question processing and answer generation can be defined here


def process_question(question):
    # Preprocess the question for more efficient searching
    processed_question = question.lower()
    processed_question = re.sub(r'[^\w\s]', '', processed_question)  # Remove punctuation
    processed_question = re.sub(r'\s+', ' ', processed_question)  # Remove extra spaces
    return processed_question

def generate_answer(processed_question, search_results):
    answer = ""

    # Example: Finding the first relevant search result that contains the question keywords
    keywords = processed_question.split()
    for result in search_results:
        if all(keyword in result.lower() for keyword in keywords):
            answer = result
            break

    return answer
