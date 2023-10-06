import requests
import json


def edition_page(secrets, edition_date):
    main_page_notionID = secrets['secrets']['parentPage_notionID']
    notion_api_key = secrets['secrets']['notion_api_key']
    key = 'Bearer ' + notion_api_key

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
        }
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
    title = page_info[0]
    link = page_info[2]
    summary = page_info[3]

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
                    "content": page_info[0]
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
                    "url": page_info[2]
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
                                "content": page_info[3]
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
        'Authorization': key
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return 0


def notion_pages(secrets, edition_date, page_info):
    parent_page_id = edition_page(secrets, edition_date)

    i = 0
    while i < len(page_info):
        subpages(secrets, page_info.iloc[i], parent_page_id)
        i += 1
    return 0
    