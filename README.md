                                                      AI-Driven Lead Automation Workflow
                                                      

![](https://github.com/ShirinMahbuba/Lead-Automation-Workflow/blob/main/Screenshot%202026-02-12%20032945.png)
![](https://github.com/ShirinMahbuba/Lead-Automation-Workflow/blob/main/Screenshot%202026-02-12%20033015.png)

                                                                       
#Assessment 1: AI Agent Workflow Automation (n8n + LLM)
📌 Project Overview
This project demonstrates an automated lead processing system built using n8n and a Large Language Model (LLM). The system intelligently captures incoming lead data, analyzes the sender's intent, extracts key information, and stores it in a structured format for business use.

🏗 Workflow Architecture
The workflow is designed to be robust and follows these steps:

Webhook Trigger: Receives raw lead messages via a POST endpoint (integrated with a Python script or API).

AI Agent Processing: Powered by the Groq Chat Model, the agent performs a deep analysis of the message.

Data Extraction: The LLM successfully identifies and categorizes the following:

Intent: Sales, Support, or Spam.

Name: Customer’s name.

Company: Organization name.

Requirement: Specific details of the inquiry.

Mock Datastore: The final structured output is appended as a new row in a Google Sheet.

🛠 Technical Implementation
💡 Prompt Strategy
I implemented a Structured Output Prompting strategy. By providing the AI with clear instructions to categorize data into specific JSON-like fields (Intent, Name, Company, Requirement), I ensured that the output is clean, consistent, and ready for database insertion without manual cleaning.

🛡 Hallucination Reduction
To minimize hallucinations, the AI Agent is configured with:

Strict Context Window: Using the Groq Chat Model with specific system instructions.

Fact-Only Extraction: I instructed the agent to extract ONLY facts explicitly mentioned in the input. If a piece of information (e.g., Company name) is missing, it is trained to return "N/A" or leave it blank rather than inventing data.

⚠️ Error-Handling Approach
Resilient Storage: Optimized the Google Sheets node using the "Append Row" operation to avoid "Match Column" errors often found in update operations.

Data Integrity: The workflow uses status monitoring across all nodes, ensuring that every lead captured by the Webhook successfully reaches the Google Sheet.

🔗 Submission Components
n8n Workflow (JSON): Exported file containing the complete logic.

Mock Datastore: Google Sheets Link

Live Webhook Endpoint: n8n Webhook URL

Demo Video: Included in the submission folder, demonstrating the end-to-end execution.

## Google Sheet :
https://docs.google.com/spreadsheets/d/1hOVZ7eWo5Q8UraFtwBLK3HSYkkrGsIXiBV4krV9m6T4/edit?usp=sharing

## Live Project Link:
https://shirinmahbuba.app.n8n.cloud/webhook/lead-intake

## Demo vedio link:
https://drive.google.com/file/d/1kbEnTRc6gCuRq5QikS2-aikeZPv4fcdz/view?usp=sharing


** The provided Webhook URL is a POST endpoint. To verify the live automation, please refer to the Demo Video where I demonstrate the data flow from the API trigger to the Google Sheets storage. **








