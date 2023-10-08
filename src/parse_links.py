import requests as r
from bs4 import BeautifulSoup as bs

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

    # The session is now logged in and can be used to retrieve content
    response = session.get(website + subfolder)

    return response.text

def parse_links(secrets, edition_date):
    subfolder = 'weeklyedition/' + edition_date

    html = get_html(secrets, subfolder)
  
    # isolate the links that in a specific section of the webpage
    start_substring = '<div class="teaser-weekly-edition--leaders css-12dw4ef ekfon2k0">'
    start_index = html.find(start_substring) + len(start_substring)
    end_index = html.find('</main>')
    sub_html = html[start_index:end_index]

    # find <a> hrefs and remove all 'aria-label' links from list
    soup = bs(sub_html, 'html.parser')
    list_of_links = soup.find_all('a', href=True)
    list_of_links = [link for i, link in enumerate(list_of_links) if not link.has_attr('aria-label')]
    
    return list_of_links