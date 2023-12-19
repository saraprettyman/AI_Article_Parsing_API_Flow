import requests
import json

def edition_page(secrets, edition_date, subheader):
    main_page_notionID = secrets['secrets']['parentPage_notionID']
    notion_api_key = secrets['secrets']['notion_api_key']
    key = 'Bearer ' + notion_api_key
    weekly_edition = "https://www.economist.com/weeklyedition/" + edition_date

    url = "https://api.notion.com/v1/pages/"

    payload = json.dumps({
        "parent": {
            "page_id": main_page_notionID
        },
        "properties": {
            "title": {
            "title": [
                {
                "type": "text",
                "text": {
                    "content": edition_date
                }
                }
            ]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "bookmark",
                "bookmark": {
                    "url": weekly_edition
                }
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": subheader
                            }
                        }
                    ]
                }
            }
        ]
        }
    )

    headers = {
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
        'Authorization': key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['id']

def subpages(secrets, page_info, parent_page_id):
    notion_api_key = secrets['secrets']['notion_api_key']
    key = 'Bearer ' + notion_api_key
    url = "https://api.notion.com/v1/pages/"
    title = page_info['title']
    article = page_info['article']
    link = page_info['link']
    summary = page_info['summary']
    

    # Design of how each subpage will look 
    payload = json.dumps(
        {
        "parent": {
            "page_id": parent_page_id
        },
        "properties": {
            "title": {
            "title": [
                {
                "type": "text",
                "text": {
                    "content": title
                }
                }
            ]
            }
        }
        ,
        "children": [
            {
                "object": "block",
                "type": "bookmark",
                "bookmark": {
                    "url": link
                }
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Questions, Research, and Vocab"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Summarization"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": summary
                            }
                        }
                    ]
                }
            }, 
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Article"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                            "type": "text",
                            "text": {
                                "content": "Article"
                            }
                        }],
                    "children": [{
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [{
                                "type": "text",
                                "text": {
                                    "content": article
                                }
                            }]
                        }
                    }]
                }
            }
        ]
            
        }
    )

    headers = {
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
        'Authorization': key
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return 0

def notion_pages(secrets, edition_date, edition_title, page_info):
    i = 0
    # create parent page
    parent_page_id = edition_page(secrets, edition_date, edition_title)

    # create subpages by going through each item in the dictionary
    while i < len(page_info):
        print(page_info[i])
    while i < len(page_info):
        subpages(secrets, page_info[i], parent_page_id)
        i += 1
    return 0
    