# Cold Email Automation (Python + Gmail SMTP)

A lightweight Python automation script for sending personalized cold emails using Gmail SMTP.  
It reads contact data from an Excel or CSV file and customizes emails for each recipient.

## Features
- Read contacts from Excel or CSV
- Personalized email content using name and company
- Secure Gmail SMTP authentication
- Console-based email delivery logs
- Simple single-folder setup

## Requirements
- Python 3.x
- Gmail account (App Password required if 2FA is enabled)

## Dependencies
pip install pandas openpyxl

## Project Structure
.
├── contacts.xlsx
├── email_script.py
└── README.md

## Contact File Format (contacts.xlsx)
First Name | Company Name | mailid
John       | OpenAI       | john@example.com
Sarah      | DataCorp     | sarah@example.org

## Usage
1. Update contacts.xlsx with recipient details
2. Open email_script.py and set YOUR_EMAIL and YOUR_PASSWORD
   Use a Gmail App Password if 2FA is enabled
3. Run the script:
   python email_script.py

## Gmail Sending Limits
Personal Gmail: 500 recipients/day  
Google Workspace: 2,000 recipients/day  
Workspace Trial: 500 recipients/day  

## Best Practices
- Add delays between emails to avoid spam detection
- Send emails in small batches (50–100 per run)
- Use Gmail API or professional email services for large-scale campaigns
