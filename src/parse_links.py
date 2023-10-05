import requests as r

def get_html(data, subfolder):
    username = data['secrets']['server_username']
    password = data['secrets']['server_password']
    
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
    
    html_content = response.text

    # Open the file in write mode
    file = open('output.html', 'w')

    # Write the HTML content to the file
    file.write(html_content)

    # Close the file
    file.close()

    return 0

def parse_links(data, edition_date):
    subfolder = 'weeklyedition/' + edition_date
    get_html(data, subfolder)
