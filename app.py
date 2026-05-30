from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        users[username] = password
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            return redirect('/dashboard')
        else:
            return "Login Failed"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

app.run(host='0.0.0.0', port=5000)