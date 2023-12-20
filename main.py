from flask import Flask, render_template, url_for, request
app = Flask(__name__, static_folder='static')


@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

@app.route('/')
def home():
    return render_template('start.html')  # Remove the leading slash

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':
    app.run()