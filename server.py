from flask import (Flask, render_template)

app = Flask(__name__)
app.secret_key = 'placeholder'

@app.route('/')
def display_homepage():
    return render_template('homepage.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)