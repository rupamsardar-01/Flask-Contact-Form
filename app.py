from flask import Flask,render_template,request,redirect,flash,url_for
import os
import smtplib
from email.mime.text import MIMEText

app= Flask(__name__)
app.secret_key="my-secret-key"

@app.route("/",methods=["GET","POST"])
def index():
    if request.method== "POST":
        name=request.form.get("name","").strip()
        email=request.form.get("email","").strip()
        message=request.form.get("message","").strip()

        send_email(name, email, message)

        flash("Form Submitted Successfully!", "success")
        return redirect(url_for("index"))

    return render_template("index.html")


def send_email(name,email,message):
    sender=os.environ.get("EMAIL_USER")
    password=os.environ.get("EMAIL_PASS")
    receiver=os.environ.get("EMAIL_USER")

    subject= "New Contact Form Submission"

    body= f""" 
    Name:{name} 
    Email:{email} 
    Message:{message} 
    """


    msg= MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=sender
    msg["To"]=receiver

    print("SENDER =", sender)
    print("PASSWORD =", password)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
    
if __name__=="__main__":
    app.run(debug=True)
