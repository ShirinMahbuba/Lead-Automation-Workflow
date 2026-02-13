                                                      AI-Driven Lead Automation Workflow
                                                      

![](https://github.com/ShirinMahbuba/Lead-Automation-Workflow/blob/main/Screenshot%202026-02-12%20032945.png)
![](https://github.com/ShirinMahbuba/Lead-Automation-Workflow/blob/main/Screenshot%202026-02-12%20033015.png)

                                                                       
## Project Overview
This project demonstrates an automated lead processing system built using n8n and a Large Language Model (LLM). It captures incoming lead data via a Webhook, uses an AI Agent to analyze intent and extract key details, and saves the structured results into Google Sheets as a mock datastore.


## Workflow Architecture
                                                                       
Webhook Trigger: Receives raw lead messages (e.g., from a Python script or API).

AI Agent Processing: Powered by the Groq Chat Model, the agent analyzes the text for specific insights.

Data Extraction: The LLM successfully identifies and categorizes:

Intent: Sales, Support, or Spam.

Name: Customer’s name.

Company: Organization name.

Requirement: Specific details of the inquiry.

Mock Datastore: The final structured output is appended as a new row in a Google Sheet.



## Technical Implementation 
                                                                      
Prompt Strategy: I implemented a Structured Output Prompting strategy. By instructing the AI to categorize the data into specific fields (Intent, Name, Company, Requirement), I ensured that the output is clean and ready for database insertion without requiring further manual cleaning.

Hallucination Reduction: To reduce hallucinations, the AI Agent is configured with a strict context window through the Groq Chat Model. I instructed the agent to only extract facts explicitly mentioned in the input message. If information is missing, it is trained to leave the field blank rather than inventing data.

Error-Handling Approach: I optimized the Google Sheets node by using the "Append Row" operation instead of "Append or Update". This avoids common "Match Column" errors that occur when a lead ID is not yet established. Additionally, the workflow shows green status indicators across all nodes, confirming data integrity from the Webhook to the final storage.


## Project Submission Components
                                                   
n8n Workflow (JSON): Exported file containing the full logic.

Mock Datastore: A Google Sheet containing the successfully stored lead data.


Demo Video: Recording of the end-to-end execution, showing the Python script trigger and the resulting row in the sheet.

## Google Sheet :
https://docs.google.com/spreadsheets/d/1hOVZ7eWo5Q8UraFtwBLK3HSYkkrGsIXiBV4krV9m6T4/edit?usp=sharing

## Live Project Link:
https://shirinmahbuba.app.n8n.cloud/webhook/lead-intake


** The provided Webhook URL is a POST endpoint. To verify the live automation, please refer to the Demo Video where I demonstrate the data flow from the API trigger to the Google Sheets storage. **







