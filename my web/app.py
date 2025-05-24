from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    EMAIL_ADDRESS = "yasasardar05@gmail.com"
    EMAIL_PASSWORD = "dsecfmuyzsskjkhz"  # Use environment variables in production for security

    msg = EmailMessage()
    msg["Subject"] = f"New message from {name}"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "yasasardar05@gmail.com"  # Change to the email you want to receive the message
    # Compose email body with sender info and message
    msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {e}"

if __name__ == '__main__':
    app.run(debug=True)
