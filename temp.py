import requests
from bs4 import BeautifulSoup

# def search_web(topic):
#     # Perform a web search using the topic
#     search_url = f'https://www.google.com/search?q={topic}'  # Replace with your preferred search engine or website
#     response = requests.get(search_url)
#     print("***********************************this is response",response)
#     if response.status_code == 200:
#         # Extract relevant information from the search results
#         soup = BeautifulSoup(response.content, 'html.parser')
#         search_results = soup.find_all('div', class_='search-result')
#         return [result.get_text() for result in search_results]
#     else:
#         return []

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


print(search_web("car"))