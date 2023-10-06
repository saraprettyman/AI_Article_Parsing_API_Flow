# Import neccessary libraries
import yaml
import pandas as pd # delete later 
from parse_links import parse_links
from parse_articles import parse_articles
from ai_summarization import ai_summarization
from notion_pages import edition_page, notion_pages

# Read YAML file
with open('config/configuration.yaml', 'r') as file:
    secrets = yaml.safe_load(file)

def main():
    # edition_date = input("What is the date for your desired weekly edition (It should be a Saturday)? Ex: YYYY-MM-DD ")
    # links = parse_links(secrets, edition_date)
    # articles = parse_articles(secrets, links).to_dict('records')
    # summaries = ai_summarization(secrets, articles)

    edition_date = "2023-10-07"
    page_info = pd.read_csv('articles1.csv').drop(columns=['Unnamed: 0'])
    notion_pages(secrets, edition_date, page_info)
    return 0
    
if __name__ == '__main__':
    main()

