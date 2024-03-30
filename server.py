from flask import (Flask, render_template)

app = Flask(__name__)
app.secret_key = 'placeholder'

@app.route('/')
def display_homepage():
    return render_template('index.html')

@app.route('/skills')
def display_skills():
    return render_template('skills.html')

@app.route('/projects')
def display_projects():
    return render_template('projects.html')

@app.route('/resume')
def display_resume():
    return render_template('resume.html')

@app.route('/contact')
def display_contact_page():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)