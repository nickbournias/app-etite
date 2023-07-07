from flask import Flask, render_template, url_for
import random
import string

app = Flask(__name__)

apps = [
    {
        'author': 'Nigel Bojangus',
        'title': 'Password Generator',
        'content': 'Password generator content'
    },
    {
        'author': 'Nigel Bojangus',
        'title': 'Test',
        'content': 'MP3 content'
    }
]

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',apps=apps)

@app.route('/about')
def about():
    title='About'
    return render_template('about.html', title=title)

@app.route('/Password Generator')
def passwordgenerator():
    length = 10  # Set the desired length of the password
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    title = 'Password Generator'
    return render_template('passwordgenerator.html', title=title, length=length, password=password)

@app.route('/Test')
def test():
    title = 'Test'
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
