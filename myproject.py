from flask import Flask, render_template, request
app = Flask(__name__)

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
        return render_template('success.html')
    return render_template('contact.html')

@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1')
