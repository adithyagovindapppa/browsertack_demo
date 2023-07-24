import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
#

def send_email(username, password, recipient_email):
    subject = "Selenium Test Execution Report"
    body = "Please find the attached test execution report."

    sender_email = username
    receiver_email = recipient_email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach the test report file
    with open('./reports/report.html', 'rb') as f:
        attach = MIMEApplication(f.read(), _subtype="html")
        attach.add_header('Content-Disposition', 'attachment', filename=str("report.html"))
        msg.attach(attach)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    gmail_username = sys.argv[1]
    gmail_password = sys.argv[2]
    recipient_email = sys.argv[3]

    subject = "Mobile automation Test Report"
    body = """
    Hi there,
    Here's the test report for the latest test run.
    Please find the attached report for more details.
    """


    send_email(gmail_username, gmail_password, recipient_email)
# import smtplib
# from email.mime.text import MIMEText
#
# def send_email(gmail_username, gmail_password, recipient_email, subject, body):
#  msg = MIMEText(body)
#  msg['Subject'] = subject
#  msg['From'] = gmail_username
#  msg['To'] = recipient_email
#
# try
#   server = smtplib.SMTP('smtp.gmail.com', 587)
#   server.starttls()
#   server.login(gmail_username, gmail_password)
#   server.sendmail(gmail_username, [recipient_email], msg.as_string())
# print("Email sent successfully.")
#     except Exception as e:\
# print(f"Error sending email: {e}")
#     finally:
# server.quit()
#
# if __name__ == "__main__":
#   import sys
# if len(sys.argv) != 6:
#   print("Usage: python send_email_script.py GMAIL_USERNAME GMAIL_PASSWORD RECIPIENT_EMAIL SUBJECT BODY")
# sys.exit(1)
#
# gmail_username = sys.argv[1]
# gmail_password = sys.argv[2]
# recipient_email = sys.argv[3]
# subject = sys.argv[4]
# body = sys.argv[5]
#
# send_email(gmail_username, gmail_password, recipient_email, subject, body)