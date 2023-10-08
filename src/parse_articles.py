import pandas as pd 
from parse_links import get_html

def parse_articles(secrets, links):
    i = 0
    articles = []
    
    # extract article and article title from html to add to list
    while i < len(links):
        html = get_html(secrets, links[i])
        start_substring = '<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width"/><title>'
        start_index = html.find(start_substring) + len(start_substring)
        end_index = html.find('</title>')

        title = html[start_index:end_index]

        start_substring = ',"articleBody":"'
        start_index = html.find(start_substring) + len(start_substring)

        article = html[start_index:html.find("■")]
        article.replace("\"", "''")
        article.replace("\n", "")

        articles.append([title, article, "https://www.economist.com/" + links[i],""])
        i += 1
     # create a dataframe with each articles information
    return pd.DataFrame(articles, columns = ["title", "article", "link", "summary"])
