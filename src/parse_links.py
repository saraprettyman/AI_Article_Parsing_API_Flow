import requests as r

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

    # Close session to free up system resources 
    r.close()

    return response.text



def parse_links(secrets, edition_date):
    subfolder = 'weeklyedition/' + edition_date

    html = get_html(secrets, subfolder)
  
    # isolate the links that in a specific section of the webpage
    start_substring = '<div class="teaser-weekly-edition--leaders css-12dw4ef ekfon2k0">'
    start_index = html.find(start_substring) + len(start_substring)
    end_index = html.find('</main>')

    sub_html = html[start_index:end_index]
    
    # find link indexes
    positions = []
    link_index = 0
    substring = '<a href="/'
    while True:
        link_index = sub_html.find(substring, link_index)
        if link_index == -1: 
            break
        link_index += len(substring)
        positions.append(link_index)

    # find links
    i = 0
    list_of_links = []
    while i < len(positions):
        sub_text = sub_html[positions[i]:]
        end_index = sub_text.find('">')
        link = sub_text[0:end_index]
        list_of_links.append(link)
        i += 1
    return list_of_links