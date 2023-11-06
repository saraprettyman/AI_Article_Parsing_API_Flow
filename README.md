# AI_Article_Parsing_API_Flow
## Description
This program summarizes weekly editions of The Economist via API Integration. A GET API request retrieves The Economist weekly edition HTML, parses for individual article links, then parse each article for the title and article body. The summarization of the article is completed through Microsoft Azure Language Services. The title, link, and summarization of the article is then put into Notion pages via Notion's Internal API Integration. 
## Getting Started
This program requires the installation of 5 packages and the set-up of 3 accounts. 
### Dependencies
The packages imported into this program are as follows:
* [YAML](yaml.org)
* [Pandas](https://pandas.pydata.org/)
* [Request](https://pypi.org/project/requests/)
* [JSON](https://docs.python.org/3/library/json.html)
* [Time](https://docs.python.org/3/library/time.html)

The YAML set up is already done in the *main.py* file of the program. The template is where you will add the values of the key-value pairs. The steps to get the values are below.  
### Microsoft Azure Language Service
The AI summarization tool used in this program a Microsoft product. To gain access, you must:
* Create a Microsoft Azure [account](https://azure.microsoft.com/en-us)
*  Go to Azure [home page](https://portal.azure.com/#home)
* Select *Create a Resource*
* Search and select *Language Services*
* After you have gone through the on-screen steps for creating the service, you will now be at your customized services page. Here, in the *Overview* tab you will see the *Endpoint* URL as well as the *Manage Keys* link
* Select the *Manage Keys* link and copy just one of the two keys. 
* The *Endpoint* URL and the *Key* will go into your YAML key vault. 

Note that your account comes with 5k request free for every 30 days. 
### Notion 
The two steps required to add pages to your Notion account are: creating an integration and creating a parent folder. Both steps require you to have Notion account and to be logged in. 

**Step 1**
1. Go to the Notion developer [page](https://www.notion.so/my-integrations).
2. Select *New Integration.*
3. Give it any name you'd like then select *Submit*.
4. In the *Secrets* tab you will find the *Internal Integration Secret.* Copy this and add it to your YAML key vault under *notion_api_key*. 
5. Under the *Capabilities* tab, ensure that *Update content*, *Read content*, *Insert content*, and *Read user information including email addresses* are all selected. 

The documentation for Notion's API can be found [here](https://developers.notion.com/docs/getting-started).  

**Step 2** 

Preferably in your browser, go to your Notion account and select the page you would like to use as the parent page (i.e where all the Notion pages you will create will be stored in). Look at URL (or copy it if you are in the application version) and select the ID that will be in the following format: 

https://www.notion.so/**parentFolderName**-**parentFolderIdNumber**

This value will be stored in your YAML file under *parentPage_notionID.*
### Economist
Given that the Economist has subscription-based content, you will need a subscribed account, which is not liked via Google sign-in but instead an email and password. These values will go into the YAML file as *server_username* and *server_password* respectively. 

## How to use
After adding the key values to the YAML file, the only user-input after that is the edition date. For the Economist, the edition day always falls on Saturday and is in the format 'YYYY-MM-DD.' From there, the servicer login information will pull the HTML file for each Economist page of that edition week, using Microsoft Azure to summarize the article (as long as it below a certain character limit) then POST the article title, link, and summary into individualized Notion pages.  