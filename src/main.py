# Import neccessary libraries
import yaml
from parse_links import parse_links


# Read YAML file
with open('config/configuration.yaml', 'r') as file:
    secrets = yaml.safe_load(file)

def main():
    edition_date = input("What is the date for your desired weekly edition (It should be a Saturday)? Ex: YYYY-MM-DD ")
    parse_links(secrets, edition_date)

if __name__ == '__main__':
    main()

