import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "youremail@gmail.com"
SENDER_PASSWORD = "abcdefghijklmnop"  # Use App Password Not Gmail Password
SUBJECT = "An email from Python"
BODY = """
Hello {name},

We hope you're doing great! 
This is an automated email.

Best regards,  
Sulav
"""

def load_receivers(file_path="receivers.csv"):
    return pd.read_csv(file_path)

def send_email(receiver_email, receiver_name):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = SUBJECT

        body_formatted = BODY.format(name=receiver_name)
        msg.attach(MIMEText(body_formatted, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Email sent to {receiver_name} ({receiver_email})")

    except Exception as e:
        print(f"Failed to send email to {receiver_name}: {e}")

def main():
    print("Sending Email...")
    recipients = load_receivers()

    for _, row in recipients.iterrows():
        send_email(row["email"], row["name"])

    print("\nAll emails sent successfully!")

if __name__ == "__main__":
    main()
