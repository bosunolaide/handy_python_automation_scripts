import requests
from bs4 import BeautifulSoup

def extract_article_titles(url):
    """
    Extracts article titles from a web page.

    :param url: URL of the web page to scrape.
    :return: List of article titles.
    """
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract article titles
    titles = []
    for header in soup.find_all(['h1', 'h2', 'h3']):  # Adjust tags as needed
        title = header.get_text(strip=True)
        if title:  # Only add non-empty titles
            titles.append(title)

    return titles

# Example usage
url = 'https://example.com/articles'
titles = extract_article_titles(url)
for i, title in enumerate(titles, start=1):
    print(f'{i}. {title}')