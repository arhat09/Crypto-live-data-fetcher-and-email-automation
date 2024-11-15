📊 Crypto Live Data Fetcher & Email Automation 📬
An automated script to fetch live cryptocurrency data and send it directly to your inbox! This project scrapes real-time cryptocurrency market data, saves it as a CSV file, and emails it to a specified recipient using Gmail's SMTP server. Ideal for anyone interested in monitoring crypto trends, tracking data for analysis, or automating data reporting.

🚀 Features
Real-Time Data Fetching: Automatically fetches the latest cryptocurrency prices and other relevant data.
Data Storage: Saves the fetched data in a CSV format with a timestamped filename.
Email Notification: Sends the generated CSV file directly to your specified email address, ensuring that you never miss a beat in the crypto world.
Customizable Schedule: Modify the code to fetch data at specific intervals as per your requirements.
Secure Authentication: Utilizes Gmail’s App Passwords for secure email authentication and enhanced privacy.
🛠️ Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/crypto-live-data-fetcher.git
cd crypto-live-data-fetcher
2. Install Dependencies
Make sure you have Python installed, and install the required packages:

bash
Copy code
pip install requests pandas smtplib
3. Configure Gmail SMTP
To set up email notifications, you’ll need to enable 2-Step Verification and generate an App Password for your Gmail account.

Go to Google Account Security.
Enable 2-Step Verification.
Go to App Passwords and create a new one for this script. Copy the generated password.
4. Update send_mail Function
In the script, replace the following variables:

sender_mail - Your Gmail address.
receiver_mail - The recipient’s email address.
email_password - Replace with your generated App Password.
💻 Usage
Simply run the script to fetch the latest crypto data and send an email:

bash
Copy code
python crypto_live_data_fetcher.py
The script will:

Fetch real-time cryptocurrency data.
Save the data as a timestamped CSV file.
Send an email with the CSV file attached.
Example Output:
plaintext
Copy code
Getting the data...
Data saved successfully: crypto_data_15-11-2024_11-23-16.csv
Email sent successfully to bhimraopetkar@gmail.com!
📧 Email Format
Subject: Crypto Data Update: <Current Date & Time>
Body: Contains information about the file and details.
Attachment: The CSV file with real-time crypto data.
🛠 Troubleshooting
535 Authentication Error: Ensure 2-Step Verification is enabled, and you’re using an App Password (not your regular Gmail password).
SMTP Port Issues: Double-check that you’re using smtp.gmail.com with port 587.
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome to improve functionality, add new features, or expand to other data sources.

📬 Contact
For questions or suggestions, reach out at your-email@example.com.

Enjoy your automated crypto updates! 💹📈

