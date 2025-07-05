# Fyndbevakning Blocket

## Beskrivning
En enkel Flask-app som bevakar fynd i Karlskoga, Degefors och Nora, och skickar mailnotiser via Gmail när det dyker upp annonser med 40-60% rabatt.

## Installation & Deployment på Railway

1. Skapa ett konto på [Railway](https://railway.app) och logga in.
2. Skapa ett nytt projekt och välj "Deploy from GitHub" eller "Upload files" (du kan använda zip-filen).
3. Ladda upp dessa filer:
    - app.py
    - requirements.txt
    - Procfile
    - README.md (valfritt)
4. Skapa en miljövariabel `GMAIL_APP_PASSWORD` med ditt Gmail app-lösenord.
   - Du måste ha tvåstegsverifiering aktiverad på Gmail.
   - Skapa app-lösenord här: https://myaccount.google.com/apppasswords
5. Starta appen via Railway.

## Användning
- Öppna den URL Railway ger dig i mobilen/webbläsaren.
- Du får mailnotiser till Babot117@gmail.com när fynd dyker upp.

---

Behöver du hjälp med Gmail app-lösenord eller annat, fråga gärna!
