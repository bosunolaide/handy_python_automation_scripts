import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_email(subject, body, to_email):
    """
    Sends an email with the specified subject and body.

    :param subject: Subject of the email.
    :param body: Body content of the email.
    :param to_email: Recipient email address.
    """
    from_email = "your_email@example.com"  # Replace with your email address
    password = "your_password"  # Replace with your email password

    # Create the email content
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port
        server.starttls()  # Secure the connection
        server.login(from_email, password)
        
        # Send the email
        server.send_message(message)
        print(f"Email sent to {to_email} at {datetime.now()}")

        # Disconnect from the server
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

def schedule_email():
    """
    Schedules the email to be sent.
    """
    subject = "Scheduled Email"
    body = "This is an automatically scheduled email."
    to_email = "recipient@example.com"  # Replace with recipient email address

    send_email(subject, body, to_email)

# Schedule the email to be sent every day at a specific time
schedule_time = "14:00"  # Replace with your desired schedule time (24-hour format)
schedule.every().day.at(schedule_time).do(schedule_email)

print(f"Email scheduler started. Will send emails every day at {schedule_time}.")

try:
    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Email scheduler stopped.")