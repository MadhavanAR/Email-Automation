# Email-Automation
# 📧 Cold Email Automation Using Python & Gmail SMTP

This project automates the process of sending personalized cold emails using Python and Gmail’s SMTP service.  
It reads contact information from an Excel sheet and sends a customized email to each recipient based on their name and company.

## 🚀 Features

- ✅ Reads contact info from an Excel or CSV file  
- ✅ Sends personalized cold emails to each contact  
- ✅ Uses Gmail SMTP with secure authentication  
- ✅ Logs email status in the terminal  
- ✅ Simple structure – all files in one folder  

## 🛠️ Prerequisites

- Python 3.x installed
- A Gmail account with **App Password** enabled (if 2FA is on)

### 📦 Required Python Libraries

Install the required libraries using pip:

```bash
pip install pandas openpyxl

```

## 📁 Files Used

All files should be in the same folder:
```
.
├── contacts.xlsx # Your contact data
├── email_script.py # The email automation script
└── README.md # This documentation
```


## 📋 contacts.xlsx Format

Ensure your spreadsheet has the following columns:

| First Name	 |  Company Name	  | mailid |
|:-----|:--------:|------:|
| John   | OpenAI | john@example.com |
| Sarah   |  DataCorp  |   	sarah@example.org |

## 🧾 How to Use

1. Prepare Your Contact List:

    - Fill in the contacts.xlsx file with recipient names, companies, and email addresses.

2. Set Your Credentials:

    - Open email_script.py.

    - Replace the YOUR_EMAIL and YOUR_PASSWORD fields.

        - Use a Gmail App Password if 2FA is on.
          
3. Run the Script:

   ```
   python email_script.py
    ```

4. Check Console Output:

    - You'll see messages like Email sent to John at john@example.com.
  
## Gmail Sending Limits

| Gmail Account Type |	| Max Recipients/Day |
|:-----|:--------:|------:|
| Personal Gmail |	| 500 |
| Google Workspace (Paid) |	| 2,000 |
| Workspace Free Trial |	| 500 |

Note: One email to 10 people = 10 recipients. Exceeding limits may block your account temporarily.

## 🧠 Tips & Recommendations

- Add a delay between emails to avoid getting flagged as spam:

```
import time
time.sleep(2)  # 2-second delay between sends
```

- For larger lists:

    - Send in batches (e.g., 50–100 emails per run).
    
    - Use logging or checkpointing to avoid duplicates if the script crashes.

- Consider using email services like SendGrid, Mailchimp, or Gmail API for sending thousands of emails.

