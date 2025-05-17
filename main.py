import pandas as pd
import smtplib
from email.message import EmailMessage

# Load data
data = pd.read_excel('contacts.xlsx')  # or pd.read_csv('contacts.csv')

# Your email credentials
YOUR_EMAIL = 'your_email@gmail.com'
YOUR_PASSWORD = 'your_app_password'  # Not your normal password if 2FA is on

# Create SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(YOUR_EMAIL, YOUR_PASSWORD)

# Loop through each contact
for index, row in data.iterrows():
    first_name = row['First Name']
    company_name = row['Company Name']
    to_email = row['mailid']

    subject = f"Ideas for {company_name}"
    body = f"""\
Hi {first_name},

I love the work you're doing at {company_name} —  
I specialize in building high-performance websites, branding, and smart AI-driven solutions for startups.

If you're planning any upgrades, scaling, or even new digital strategies,  
I'd love to share a few ideas — no obligation, just adding value.

Would you be open for a quick chat this week?

Best regards,  
Madhavan A
"""

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = YOUR_EMAIL
    msg['To'] = to_email
    msg.set_content(body)

    try:
        server.send_message(msg)
        print(f"Email sent to {first_name} at {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Close the server
server.quit()
