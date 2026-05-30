from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application instance
app = Flask(__name__)

# Your custom authorized credentials dictionary
USER_DATABASE = {
    "Syed Ali Haider": "SyedAli157"
}

# Route for the home page / login screen
@app.route('/')
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# Route that processes the form submission credentials
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if the username exists and password matches exactly
    if username in USER_DATABASE and USER_DATABASE[username] == password:
        return render_template('success.html')
    else:
        return render_template('failed.html')

# Simple placeholder for registration route
@app.route('/register')
def register():
    return '<h2 style="font-family:sans-serif; text-align:center; margin-top:50px; color:#1c2541;">Registration system base key is currently being compiled by Syed Ali Haider! 👑</h2>'

# Main runner config
if __name__ == '__main__':
    app.run(debug=True, port=5000)