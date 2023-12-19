from bs4 import BeautifulSoup
import pandas as pd
from parse_links import get_html

def parse_articles(secrets, article_links):
    articles = []
    for category in article_links:
        for link in article_links[category]:
            articles.append(parse_article(secrets, link, category))

    return pd.DataFrame(articles, columns=["category", "title", "article", "link", "summary"])

def parse_article(secrets, link, category):
    # Get the HTML content of the article
    html = get_html(secrets, link)
    soup = BeautifulSoup(html, 'html.parser')

    # title
    title = soup.find('title').string

    # body 
    article = ""
    paragraphs = soup.find_all(lambda tag: tag.name == 'p' and tag.get('data-component') == 'paragraph')
    for paragraph in paragraphs:
        article += paragraph.text + "\n\n"
    article = article.replace('\"', '"').replace("\n", "").replace("\\n", "").replace('"\ ','"').replace('\xa0', ' ')

    return [category, title, article, "https://www.economist.com" + link, ""]

