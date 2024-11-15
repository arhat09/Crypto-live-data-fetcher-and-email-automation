# This function gets the real-time cryptocurrency price every day at 8 am,
# identifies the top 10 cryptos, and sends emails.
# It also saves the data as a CSV file.

# Using `requests`, we send a request to the website to get the data.
# Once we get the data, we capture it and store it.

# Importing dependencies
import smtplib  # Connects and sends emails.
from email.mime.text import MIMEText  # Specifies the body of the email.
from email.mime.multipart import MIMEMultipart  # Organizes body and attachments into a single email object.
from email.mime.base import MIMEBase  # Handles the attachment content.
import email.encoders  # Ensures attachments are properly encoded for safe delivery.

import requests
import schedule
import pandas as pd
from datetime import datetime  # Captures the date and time when data is collected.
import time

# Function to send an email with the specified subject, body, and filename.
def send_mail(subject, body, filename):
    smtp_server = "smtp.gmail.com"         # Gmail's SMTP server
    smtp_port = 587                        # Standard port for email submission with encryption
    sender_mail = "thearhat09@gmail.com"   # Your email address
    email_password = "veqn ysnv jzvk xdeh"    # Your Gmail password (or App Password)
    receiver_mail = "bhimraopetkar@gmail.com"  # Recipient's email

    # Compose email
    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = receiver_mail
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Attach CSV file
    with open(filename, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        email.encoders.encode_base64(part)  # Encodes the file in base64 (optional)
        part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
        message.attach(part)

    # Start the server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection
            server.login(sender_mail, email_password)  # Login

            # Send email
            server.sendmail(sender_mail, receiver_mail, message.as_string())
            print("Email sent successfully!")
        
    except Exception as e:
        print(f'Unable to send mail: {e}')

# Function to get crypto data, save it, and send via email
def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    
    # Define parameters for the API request
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 250,
        'page': 1
    }

    # Sending request to get data
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Connection successful! \nGetting the data...")

        # Storing the response in JSON format
        data = response.json()
        df = pd.DataFrame(data)

        # Selecting only necessary columns
        df = df[['id', 'current_price', 'market_cap', 'price_change_percentage_24h', 'high_24h', 'low_24h', 'ath', 'atl']]

        # Create a timestamp
        today = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        df['time_stamp'] = today

        # Filter top 10 gainers and losers based on 24-hour price change
        top_10_negative = df.nsmallest(10, 'price_change_percentage_24h')
        top_10_positive = df.nlargest(10, 'price_change_percentage_24h')

        # Save the DataFrame to a CSV file
        file_name = f'crypto_data_{today}.csv'
        df.to_csv(file_name, index=False)
       
        print(f"Data saved successfully: {file_name}")

        # Call email function to send the reports
        subject = f"Top 10 Cryptocurrency Data to Invest - {today}"
        body = f"""
        Good Morning!\n\n
        Your crypto report is here!\n\n
        Top 10 cryptocurrencies with the highest price increase in the last 24 hours:\n
        {top_10_positive}\n\n\n
        Top 10 cryptocurrencies with the highest price decrease in the last 24 hours:\n
        {top_10_negative}\n\n\n
        Attached is a report with data for 250+ cryptocurrencies.\n\n
        Regards,\n
        Your Crypto Python Application
        """
        send_mail(subject, body, file_name)

    else:
        print(f"Connection failed with error code {response.status_code}")

# If the script is run directly, execute the get_crypto_data function
if __name__ == '__main__':
    get_crypto_data()
  

  # sheduling the task at 8AM
    # schedule.every().day.at('08:00').do(get_crypto_data)
    schedule.every().day.at('16:26').do(get_crypto_data)
    
    while True:
        schedule.run_pending()
        time.sleep(60)