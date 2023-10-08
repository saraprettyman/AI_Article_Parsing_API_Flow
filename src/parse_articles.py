import pandas as pd 
from parse_links import get_html

def parse_articles(secrets, links):
    articles = [parse_article(secrets, link) for link in links]

    # Create a dataframe with each article's information
    return pd.DataFrame(articles, columns=["title", "article", "link", "summary"])

def parse_article(secrets, link):
    # Get the HTML content of the article
    html = get_html(secrets, link)

    # Extract the title
    start_substring = '<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width"/><title>'
    start_index = html.find(start_substring) + len(start_substring)
    end_index = html.find('</title>')
    title = html[start_index:end_index]

    # Extract the article
    start_substring = ',"articleBody":"'
    start_index = html.find(start_substring) + len(start_substring)
    article = html[start_index:html.find("■")]
    
    # Replace unnecessary characters
    article = article.replace("\"", "''").replace("\n", "").replace("\\n", "")

    # Return the article information
    return [title, article, "https://www.economist.com" + link, ""]
