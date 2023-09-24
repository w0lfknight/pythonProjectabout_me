import os
import smtplib

from flask import Flask, render_template, request

app = Flask(__name__)

MY_EMAIL = 'ajay20003kumar@gmail.com'
MY_PASSWORD = os.environ.get('PASSWORD')
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form.get("username")
        email = request.form.get("email_id")
        website = request.form.get("website")
        message = request.form.get("message")
        if not website:
            website = "not available"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,

                msg=f"Subject:This is the feed back you got from a user!\n\nHis name is:{name}\n "
                    f"His email is {email}\n"
                    f"His website is {website}\n"
                    f"And he wants to say to you that:{message}"
            )

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)