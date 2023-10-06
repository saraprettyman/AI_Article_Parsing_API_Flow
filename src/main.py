# Import neccessary libraries
import yaml
import pandas as pd # delete later 
from parse_links import parse_links
from parse_articles import parse_articles
from ai_summarization import ai_summarization

# Read YAML file
with open('config/configuration.yaml', 'r') as file:
    secrets = yaml.safe_load(file)

def main():
    edition_date = input("What is the date for your desired weekly edition (It should be a Saturday)? Ex: YYYY-MM-DD ")
    links = parse_links(secrets, edition_date)
    articles = parse_articles(secrets, links).to_dict('records')
    summaries = ai_summarization(secrets, articles)
    notion_pages = parse_links(secrets, edition_date, summaries)
    notion_pages
    return 0
    
if __name__ == '__main__':
    main()

