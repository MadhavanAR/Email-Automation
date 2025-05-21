import pandas as pd
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load data
data = pd.read_excel('contacts.xlsx')  # or pd.read_csv('contacts.csv')

# Your email credentials
YOUR_EMAIL = 'amadhav693@gmail.com'
YOUR_PASSWORD = 'lejh owmy jlzc byzv'  # Not your normal password if 2FA is on

# Create SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(YOUR_EMAIL, YOUR_PASSWORD)

# Loop through each contact
for index, row in data.iterrows():
    first_name = row['First Name']
    company_name = row['Company Name']
    to_email = row['mailid']

    subject = f"Strategic Digital Advancement for {company_name}"
    
    # Create a multipart message for HTML support
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Madhavan A <' + YOUR_EMAIL + '>'
    msg['To'] = to_email
    
    # Plain text version of your email
    text_content = f"""\
Hi {first_name},

I've been following {company_name} and noticed your commitment to innovation.

I create digital solutions that are specifically tailored to your audience – combining technical expertise with a deep understanding of what makes your customers engage.

Services:
- Performance Optimization
- Brand Identity Systems
- AI Business Integration
- Responsive Applications

What makes our potential collaboration unique is my commitment to understand your vision first, then create solutions that resonate with your specific audience – not just implementing technology for technology's sake.

I have ideas specifically for {company_name} that I believe could transform how your customers experience your brand.

Could we connect for 15 minutes this week?

Madhavan A
Founder & Digital Strategist, Chen AI

Portfolio: https://chen-ai.vercel.app/
LinkedIn: https://www.linkedin.com/in/madhavan25
Company Profile: https://www.linkedin.com/company/chenai
"""
    
    # HTML version of your email with strategic visual highlighting
    html_content = f"""\
<html>
<head>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            line-height: 1.5;
            color: #333333;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }}
        .container {{
            padding: 20px;
        }}
        .header {{
            border-left: 3px solid #2C3E50;
            padding-left: 15px;
            margin-bottom: 20px;
        }}
        .highlight-box {{
            background-color: #f8f9fa;
            padding: 15px;
            margin: 20px 0;
        }}
        .service-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 20px 0;
        }}
        .service-card {{
            background-color: #f8f9fa;
            padding: 12px 15px;
        }}
        .key-point {{
            color: #3498DB;
            font-weight: 600;
        }}
        .cta-section {{
            text-align: center;
            padding: 20px 0;
            margin: 25px 0;
            border-top: 1px solid #e0e0e0;
            border-bottom: 1px solid #e0e0e0;
        }}
        .cta-text {{
            font-size: 16px;
            color: #333333;
        }}
        .signature {{
            margin-top: 25px;
            padding-top: 15px;
            border-top: 1px solid #EEEEEE;
        }}
        .links {{
            margin-top: 15px;
        }}
        .links a {{
            color: #333333;
            text-decoration: none;
            margin-right: 15px;
        }}
        .links a:hover {{
            text-decoration: underline;
            color: #3498DB;
        }}
        h2 {{
            margin-bottom: 10px;
        }}
        p {{
            margin: 10px 0;
        }}
        .emotional-connect {{
            font-style: italic;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>Hi {first_name},</h2>
        </div>
        
        <p>I've been following {company_name} and noticed your commitment to innovation.</p>
        
        <div class="highlight-box">
            I create digital solutions that are <span class="key-point">specifically tailored to your audience</span> – combining technical expertise with a deep understanding of <span class="key-point">what makes your customers engage</span>.
        </div>
        
        <div class="service-grid">
            <div class="service-card">Performance Optimization</div>
            <div class="service-card">Brand Identity Systems</div>
            <div class="service-card">AI Business Integration</div>
            <div class="service-card">Responsive Applications</div>
        </div>
        
        <p class="emotional-connect">What makes our potential collaboration unique is my commitment to <span class="key-point">understand your vision first</span>, then create solutions that <span class="key-point">resonate with your specific audience</span> – not just implementing technology for technology's sake.</p>
        
        <div class="cta-section">
            <div class="cta-text">
                I have ideas specifically for {company_name} that I believe could <span class="key-point">transform how your customers experience your brand</span>.<br><br>
                Could we connect for 15 minutes this week?
            </div>
        </div>
        
        <div class="signature">
            <p>
            <strong>Madhavan A</strong><br>
            Founder & Digital Strategist, Chen AI
            </p>
            
            <div class="links">
                <a href="https://chen-ai.vercel.app/">Portfolio</a>
                <a href="https://www.linkedin.com/in/madhavan25">LinkedIn</a>
                <a href="https://www.linkedin.com/company/chenai">Company Profile</a>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    # Attach parts to the message
    part1 = MIMEText(text_content, 'plain')
    part2 = MIMEText(html_content, 'html')
    msg.attach(part1)
    msg.attach(part2)

    try:
        server.send_message(msg)
        print(f"Email sent to {first_name} at {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Close the server
server.quit()

# import pandas as pd
# import smtplib
# from email.message import EmailMessage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Load data
# data = pd.read_excel('contacts.xlsx')  # or pd.read_csv('contacts.csv')

# # Your email credentials
# YOUR_EMAIL = 'amadhav693@gmail.com'
# YOUR_PASSWORD = 'lejh owmy jlzc byzv'  # Not your normal password if 2FA is on

# # Create SMTP session
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(YOUR_EMAIL, YOUR_PASSWORD)

# # Loop through each contact
# for index, row in data.iterrows():
#     first_name = row['First Name']
#     company_name = row['Company Name']
#     to_email = row['mailid']

#     subject = f"Innovative Solutions for {company_name}"
    
#     # Create a multipart message for HTML support
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = subject
#     msg['From'] = 'Madhavan A <' + YOUR_EMAIL + '>'
#     msg['To'] = to_email
    
#     # Plain text version of your email
#     text_content = f"""\
# Hi {first_name},

# I noticed the impressive work you're doing at {company_name}, and I wanted to reach out.

# I specialize in creating high-performance websites, strategic branding, and innovative AI-driven solutions that help startups scale efficiently. My approach combines technical expertise with creative design thinking to deliver solutions that not only work flawlessly but also captivate users.

# If you're considering digital upgrades, scaling challenges, or exploring new tech strategies, I'd love to share some tailored ideas specific to your industry — no obligation, just adding value.

# Would you be open for a quick 15-minute chat this week?

# Learn more about my work:
# - Portfolio: https://chen-ai.vercel.app/
# - LinkedIn: https://www.linkedin.com/in/madhavan25
# - YouTube: https://www.youtube.com/@Madhavan_ChenAi

# Looking forward to connecting,
# Madhavan A
# Founder, Chen AI
# """
    
#     # HTML version of your email with visual enhancements
#     html_content = f"""\
# <html>
# <head>
#     <style>
#         body {{
#             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#             line-height: 1.6;
#             color: #333333;
#             max-width: 600px;
#             margin: 0 auto;
#         }}
#         .header {{
#             border-left: 4px solid #4285F4;
#             padding-left: 15px;
#             margin: 20px 0;
#         }}
#         .highlight {{
#             background-color: #F8F9FA;
#             border-radius: 5px;
#             padding: 15px;
#             margin: 15px 0;
#         }}
#         .signature {{
#             margin-top: 30px;
#             padding-top: 15px;
#             border-top: 1px solid #EEEEEE;
#         }}
#         .social-links {{
#             margin-top: 15px;
#         }}
#         .social-links a {{
#             color: #4285F4;
#             text-decoration: none;
#             margin-right: 15px;
#         }}
#         .social-links a:hover {{
#             text-decoration: underline;
#         }}
#         .tagline {{
#             font-style: italic;
#             color: #777777;
#         }}
#         .emoji {{
#             font-size: 18px;
#             vertical-align: middle;
#             margin-right: 5px;
#         }}
#     </style>
# </head>
# <body>
#     <div class="header">
#         <h2>Hi {first_name},</h2>
#     </div>
    
#     <p>I noticed the impressive work you're doing at <strong>{company_name}</strong>, and I wanted to connect.</p>
    
#     <div class="highlight">
#         <p><span class="emoji">🚀</span> I specialize in creating <strong>high-performance websites</strong>, <strong>strategic branding</strong>, and <strong>innovative AI-driven solutions</strong> that help startups scale efficiently.</p>
        
#         <p>My approach combines technical expertise with creative design thinking to deliver solutions that not only work flawlessly but also captivate users and drive business growth.</p>
#     </div>
    
#     <p>If you're considering any of these for {company_name}:</p>
#     <ul>
#         <li><span class="emoji">⚡</span> Website performance optimization</li>
#         <li><span class="emoji">🎨</span> Brand identity refinement</li>
#         <li><span class="emoji">🤖</span> AI integration for business processes</li>
#         <li><span class="emoji">📱</span> Responsive app development</li>
#     </ul>
    
#     <p>I'd love to share some tailored ideas specific to your industry — <em>no obligation</em>, just adding value.</p>
    
#     <p>Would you be open for a quick 15-minute chat this week?</p>
    
#     <div class="signature">
#         <p>Looking forward to connecting,<br>
#         <strong>Madhavan A</strong><br>
#         <span class="tagline">Founder, Chen AI</span></p>
        
#         <div class="social-links">
#             <p>
#                 <a href="https://chen-ai.vercel.app/">Portfolio Website</a> | 
#                 <a href="https://www.linkedin.com/in/madhavan25">LinkedIn</a> | 
#                 <a href="https://www.youtube.com/@Madhavan_ChenAi">YouTube</a>
#             </p>
#         </div>
#     </div>
# </body>
# </html>
# """
    
#     # Attach parts to the message
#     part1 = MIMEText(text_content, 'plain')
#     part2 = MIMEText(html_content, 'html')
#     msg.attach(part1)
#     msg.attach(part2)

#     try:
#         server.send_message(msg)
#         print(f"Email sent to {first_name} at {to_email}")
#     except Exception as e:
#         print(f"Failed to send email to {to_email}: {e}")

# # Close the server
# server.quit()
