import smtplib
from email.mime.text import MIMEText
from flask import Flask, request

app = Flask(__name__)

SENDER = "yourgmail@gmail.com"
PASSWORD = "your_app_password"
RECEIVER = "yourgmail@gmail.com"

@app.route("/fault", methods=["POST"])
def fault():
    msg = MIMEText("Power Fault Detected")
    msg["Subject"] = "ESP8266 ALERT"
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(SENDER, PASSWORD)
    s.send_message(msg)
    s.quit()
    return "Email Sent"

app.run(host="0.0.0.0", port=5000)
