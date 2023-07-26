import yagmail
import random
import datetime
import requests
import json

# Define your data
marketing_quotes = [
    "Marketing quote 1",
    "Marketing quote 2",
    "Marketing quote 3",
    # Add more marketing quotes as needed
]

company_news = [
    {"news": "Company news 1", "details": "Details of company news 1"},
    {"news": "Company news 2", "details": "Details of company news 2"},
    # Add more company news items as needed
]

product_lineup = [
    {"product": "Product 1", "description": "Description of product 1"},
    {"product": "Product 2", "description": "Description of product 2"},
    # Add more product lineup items as needed
]

# List of email addresses
email_list = ['your_email1@example.com', 'your_email2@example.com', 'your_email3@example.com']

# Your credentials
yag = yagmail.SMTP('your_email@gmail.com', 'your_email_password')

def send_email():
    # Select a random marketing quote, company news, and product lineup
    marketing_quote = random.choice(marketing_quotes)
    company_news_item = random.choice(company_news)
    product_lineup_item = random.choice(product_lineup)

    # Prepare email content
    contents = [
        f"Today's marketing quote:\n\n{marketing_quote}\n",
        f"Today's company news:\n\n{company_news_item['news']}: {company_news_item['details']}\n",
        f"Today's product lineup:\n\n{product_lineup_item['product']}: {product_lineup_item['description']}\n"
    ]

    # Prepare email subject
    subject = f"The Marketing Email - {datetime.date.today().strftime('%B %d, %Y')}"

    # Send email to each email address
    for email in email_list:
        yag.send(email, subject, contents)

# Call the function to send the marketing email to multiple recipients
send_email()
