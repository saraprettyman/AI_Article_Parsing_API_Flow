import requests as r
import pandas as pd

def post_api_query(azure_api_key, article):
    import requests
    import json

    url = "https://power-economist.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2023-04-01"

    payload = json.dumps(
        {
            "displayName": "Document Abstractive Summarization Task",
            "analysisInput": {
                "documents": [
                {
                    "id": "1",
                    "language": "en",
                    "text": article
                }
                ]
            },
            "tasks": [
                {
                "kind": "AbstractiveSummarization",
                "taskName": "Document Abstractive Summarization Task 1",
                "parameters": {
                    "sentenceCount": 15
                }
                }
            ]
        }
    )
    headers = {
        'Ocp-Apim-Subscription-Key': azure_api_key,
        'Content-Type': 'application/json'
    }

    return r.request("POST", url, headers=headers, data=payload)

def get_api_query(azure_api_key, op_location):
    payload = {}

    headers = {
        'Ocp-Apim-Subscription-Key': azure_api_key,
        'Content-Type': 'application/json'
    }

    return r.request("GET", op_location, headers=headers, data=payload)


def ai_summarization(secrets, articles):
    i = 0
    azure_api_key = secrets['secrets']['azure_api_key']

    while i < len(articles):
        # post query to azure, get operation location url 
        op_location = post_api_query(azure_api_key, articles[i]['article']).headers['Operation-Location']

        # retrieve response from operation location url
        in_progress = True
        while in_progress:
            get_response = get_api_query(azure_api_key, op_location).text
            if get_response.find('inProgress":1') == -1:
                in_progress = False
        
        # parse response, add to data table
        start_substring = '"text":"'
        start_index = get_response.find(start_substring) + len(start_substring)
        end_index = get_response.find('","contexts":')
        articles[i]['summary'] = get_response[start_index:end_index]

        i+=1
    # dict form is no longer required; return to dataframe
    return pd.DataFrame(articles)