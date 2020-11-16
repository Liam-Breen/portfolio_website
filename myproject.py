from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail= Mail(app)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route("/")
def render_home_page():
    return render_template('home.html')

@app.route("/projects")
def render_projects():
     return render_template('projects.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    data = request.form
    if data:
        send_email(data)
        return render_template('success.html')
    return render_template('contact.html')

def send_email(data):
    print(data['name'])
    try:
        msg = Message(f'{data["subject"]}', sender = f'{data["email"]}', recipients = ['liam.breen25@gmail.com'])
        msg.body = f"name: {data['name']}, email: {data['email']}, sender: {data['email']}, message: {data['message']},"
        mail.send(msg)
    except:
        pass



@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1')
