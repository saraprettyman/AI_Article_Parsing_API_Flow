# Import libraries
import yaml
import re
from parse_links import parse_for_links
from parse_articles import parse_articles
from ai_summarization import ai_summarization
from notion_pages import notion_pages

# Read YAML file
with open('config/configuration.yaml', 'r') as file:
    secrets = yaml.safe_load(file)

def main():
    edition_date = input("What is the date for your desired weekly edition (It should be a Saturday)? Ex: YYYY-MM-DD ")

    if (re.search('\d{4}-\d{2}-\d{2}', edition_date) == None):
        print("Invalid date format. Please try again.")
        return 0
    
    edition_title, links = parse_for_links(secrets, edition_date)
    articles = parse_articles(secrets, links).to_dict('records') # Convert to dictionary for easier changes
    articles = ai_summarization(secrets, articles)
    notion_pages(secrets, edition_date, edition_title, articles)
    return 0
    
if __name__ == '__main__':
    main()

