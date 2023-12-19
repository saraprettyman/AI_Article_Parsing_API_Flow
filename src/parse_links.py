from bs4 import BeautifulSoup
import requests as r
import logging as log

def get_html(secrets, subfolder):
    username = secrets['secrets']['server_username']
    password = secrets['secrets']['server_password']
    
    website = "https://www.economist.com/"

    # Create a session object
    session = r.Session()

    # Define login parameters
    payload = {
        'username': username,
        'password': password
    }

    # Send a POST request to the login URL with the parameters
    response = session.post(website, data=payload)
    
    try:
    # The session is now logged in and can be used to retrieve content
        response = session.get(website + subfolder)
        response.raise_for_status()
    except r.exceptions.TooManyRedirects:
        log.info("Page html retrival failed. Skipping...")
        log.info("Page failed", website + subfolder)
        return None
    return response.text

def find_category_links(links, category):
    return list(set(link for link in links if link.startswith('/' + category + '/')))

def parse_for_links(secrets, edition_date):
    subfolder = 'weeklyedition/' + edition_date

    html = get_html(secrets, subfolder)

    soup = BeautifulSoup(html, 'html.parser')
    article_links = {}

    title = soup.find('title').string
    links = [a['href'] for a in soup.find_all('a', href=True)]

    categories = ['leaders', 'by-invitation', 'briefing', 'united-states', 'the-americas', 'asia', 
                'china', 'middle-east-and-africa', 'europe', 'britain', 'international', 'business',
                'finance-and-economics', 'science-and-technology', 'culture', 
                'economic-and-financial-indicators', 'obituary']

    for category in categories:
        article_links[category] = find_category_links(links, category)

    return title, article_links
