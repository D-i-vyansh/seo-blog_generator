from googlesearch import search  # Importing Google Search to fetch trending topics
import requests  # Importing requests to fetch web pages
from bs4 import BeautifulSoup  # Importing BeautifulSoup for web scraping

def get_trending_hr_topics():
    """
    Prompts the user to enter a specific HR topic or fetches general HR trends 
    from trusted websites like Forbes, LinkedIn, and HR.com.
    
    Returns:
        list: A list of URLs from Google search results.
    """
    
    # Taking user input for a specific HR topic
    user_input = input("Enter a specific HR topic or leave blank for general trends: ").strip()
    
    # Defining the base query for HR trends from reliable sources
    base_query = "latest HR trends site:forbes.com OR site:linkedin.com OR site:hr.com"
    
    # If the user provides a topic, append it to the query
    query = f"{user_input} {base_query}" if user_input else base_query
    
    # Performing a Google search and fetching top 5 results
    results = list(search(query, num_results=5))
    return results


def extract_content(url):
    """
    Extracts text content from the given URL using web scraping.
    
    Args:
        url (str): The URL of the webpage to scrape.
    
    Returns:
        str: Extracted text content from the webpage (limited to 3000 characters).
    """
    
    try:
        # Sending a GET request to the URL with a user-agent to avoid bot detection
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        
        # Parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extracting all paragraph (<p>) tags from the webpage
        paragraphs = soup.find_all('p')
        
        # Joining all paragraph texts into a single string
        content = "\n".join([para.get_text() for para in paragraphs])
        
        # Limiting the extracted content to 3000 characters
        return content[:3000]
    
    except requests.exceptions.HTTPError as http_err:
        # Handling HTTP errors (e.g., 404 Not Found, 403 Forbidden)
        return f"HTTP error occurred: {http_err}"
    
    except Exception as e:
        # Handling any other errors during the request or scraping process
        return f"Error fetching content: {str(e)}"
        

def research():
    """
    Conducts research by searching for trending HR topics and extracting their content.
    
    Returns:
        str: Combined text content from multiple sources.
    """
    
    print("Making a search for trending topics.....")
    
    # Fetch URLs for trending HR topics
    urls = get_trending_hr_topics()
    
    print("Extracting the content from extracted URLs....")
    
    # Extract content from each fetched URL
    extracted_text = [extract_content(url) for url in urls]
    
    # Joining extracted content from all URLs into a single text
    return "\n\n".join(extracted_text)
