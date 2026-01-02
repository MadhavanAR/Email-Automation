Cold Email Automation (Python + Gmail SMTP)

A lightweight Python script to send personalized cold emails at scale using Gmail SMTP.
Contacts are read from an Excel/CSV file and emails are customized per recipient.

Features
	•	Read contacts from Excel or CSV
	•	Personalized email content (name, company)
	•	Secure Gmail SMTP authentication
	•	Console-based delivery status logs
	•	Simple, single-folder setup

Requirements
	•	Python 3.x
	•	Gmail account (App Password required if 2FA is enabled)

Dependencies

pip install pandas openpyxl

Project Structure

.
├── contacts.xlsx
├── email_script.py
└── README.md

Contact File Format (contacts.xlsx)

First Name	Company Name	mailid
John	OpenAI	john@example.com
Sarah	DataCorp	sarah@example.org

Usage
	1.	Update contacts.xlsx with recipient data
	2.	Set YOUR_EMAIL and YOUR_PASSWORD in email_script.py
	•	Use a Gmail App Password if 2FA is enabled
	3.	Run the script:

python email_script.py

Gmail Sending Limits

Account Type	Max Recipients/Day
Personal Gmail	500
Google Workspace	2,000
Workspace Trial	500

Best Practices
	•	Add delays between emails to avoid spam detection
	•	Send in small batches (50–100 emails per run)
	•	Use professional email services or Gmail API for large-scale campaigns
