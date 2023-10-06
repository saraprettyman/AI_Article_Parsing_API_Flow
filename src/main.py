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
    
        # commenting out to save time
        #links = parse_links(secrets, edition_date)
        # articles = parse_articles(secrets, links)
    
    articles = pd.read_csv("articles.csv")
    ai_summarization(secrets, articles)
if __name__ == '__main__':
    main()

