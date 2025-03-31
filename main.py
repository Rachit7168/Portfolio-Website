from flask import Flask, render_template , request
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/contact', methods = ['POST'])
def contact():
    email = request.form.get('email')
    message = request.form.get('message')
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="rachitmakwana15@gmail.com",
                msg=f"Subject:Customer Inquiry\n\nCustomer email: {email}\nMessage: {message}"
            )
        return "Form submitted successfully!"
    except Exception as e:
        print(f'Error Sending email : {e}')
        return "Failed to send mail"

if __name__ == "__main__":  
    app.run(debug=True)  
