import requests as r
import pandas as pd
import json
import time

def post_api_query(secrets, article):
    azure_api_key = secrets['secrets']['azure_api_key']
    service_endpoint = secrets['secrets']['azure_service_endpoint']

    # This URL is specific to my Azure account. You will need to create your own.
    url = service_endpoint + "language/analyze-text/jobs?api-version=2023-04-01"

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
        print('Summarizing article ' + str(i + 1) + ' of ' + str(len(articles)) + ' [' + articles[i]['title'] + ']')
        post_response = post_api_query(secrets, articles[i]['article'])
        time.sleep(5)
        if post_response.status_code == 202:
            op_location = post_response.headers['Operation-Location']

            # retrieve response from operation location url, wait til response is complete
            in_progress = True
            while in_progress:
                get_response = get_api_query(azure_api_key, op_location).text
                if get_response.find('inProgress":1') == -1:
                    in_progress = False
                else: 
                    time.sleep(15)

            # parse response, add to data table. Check for errors
            start_substring = '"text":"'
            start_index = get_response.find(start_substring) + len(start_substring)
            end_index = get_response.find('","contexts":')
            
            if end_index == -1:
                articles[i]['summary'] = 'Invalid request.'
            else: 
                articles[i]['summary'] = get_response[start_index:end_index]
        else: 
            articles[i]['summary'] = 'Text is too long. Must use another AI tool to summarize.'
        i+=1
    # dict form is no longer required; return to dataframe
    return articles