from flask import Flask, render_template_string
import smtplib
from email.mime.text import MIMEText
import threading
import time
import os

app = Flask(__name__)

MAIL_TO = "Babot117@gmail.com"
MAIL_FROM = "Babot117@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = MAIL_FROM
SMTP_PASS = os.getenv("GMAIL_APP_PASSWORD")  # App-lösenord sätts som miljövariabel

annonser = [
    {"titel": "Ryggsäck Asaklitt", "plats": "Karlskoga", "pris": 400, "nypris": 1000},
    {"titel": "Tält retro", "plats": "Degefors", "pris": 700, "nypris": 2000},
    {"titel": "TV-bänk IKEA", "plats": "Nora", "pris": 150, "nypris": 1200},
]

def send_mail(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = MAIL_FROM
    msg["To"] = MAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(MAIL_FROM, [MAIL_TO], msg.as_string())
        print(f"Mail skickat till {MAIL_TO}")
    except Exception as e:
        print(f"Fel vid sändning av mail: {e}")

def check_fynd():
    while True:
        for annons in annonser:
            rabatt = (1 - annons["pris"] / annons["nypris"]) * 100
            if 40 <= rabatt <= 60:
                subject = f"Fynd i din region: {annons['titel']} för {annons['pris']} kr"
                body = f"Annonsen finns i {annons['plats']}.
Pris: {annons['pris']} kr
Nypris: {annons['nypris']} kr
Rabatt: {rabatt:.1f}%"
                send_mail(subject, body)
        time.sleep(3600)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="sv">
    <head>
        <meta charset="UTF-8" />
        <title>Fyndbevakning Blocket</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style>
            body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: #333; margin: 0; padding: 2rem;}
            h1 { color: white; }
            .content { background: white; padding: 2rem; border-radius: 8px; max-width: 600px; margin: auto; }
            .annons { margin-bottom: 1rem; padding-bottom: 1rem; border-bottom: 1px solid #ccc; }
            @media (max-width: 600px) {
                body { padding: 1rem; }
                .content { padding: 1rem; }
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>Välkommen till Fyndbevakning Blocket!</h1>
            <p>Du får mailnotiser till <strong>{{ mail }}</strong> när en annons i Karlskoga, Degefors eller Nora dyker upp med 40-60% rabatt jämfört med nypris.</p>
            <h2>Senaste annonser (simulerade):</h2>
            {% for a in annonser %}
            <div class="annons">
                <strong>{{ a.titel }}</strong><br />
                Plats: {{ a.plats }}<br />
                Pris: {{ a.pris }} kr (Nypris: {{ a.nypris }} kr)<br />
                Rabatt: {{ "%.1f"|format((1 - a.pris/a.nypris)*100) }}%
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """, mail=MAIL_TO, annonser=annonser)

if __name__ == "__main__":
    threading.Thread(target=check_fynd, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
