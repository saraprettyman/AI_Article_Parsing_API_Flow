import pandas as pd 
from parse_links import get_html

def parse_articles(secrets, links):
    # loop through links
    i = 0
    articles = []
    while i < len(links):
        html = get_html(secrets, links[i])
        start_substring = '<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width"/><title>'
        start_index = html.find(start_substring) + len(start_substring)
        end_index = html.find('</title>')

        title = html[start_index:end_index]

        start_substring = ',"articleBody":"'
        start_index = html.find(start_substring) + len(start_substring)
        html = html[start_index:]
        end_index = html.find('","')
        
        article = html[start_index:end_index]
        print(article)
        articles.append([title, article, "https://www.economist.com/" + links[i],""])
        i += 1
    return pd.DataFrame(articles, columns = ["title", "article", "link", "summary"])
