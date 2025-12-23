import smtplib
from email.mime.text import MIMEText
from flask import Flask, request

app = Flask(__name__)

SENDER = "manbu3954@gmail.com"
PASSWORD = "Project@1234"
RECEIVER = "harikumar.p.2026@rkmshome.org"

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
