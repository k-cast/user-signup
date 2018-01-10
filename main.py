from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

form = ''

@app.route('/')
def display_user_signup_form():
    return render_template('form.html', title = "Signup", username_error='', password_error='', verify_error='', email_error='')

@app.route('/', methods=['POST', 'GET'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ''
    un_error = "That's not a valid username"
    password_error = ''
    pw_error = "That's not a valid password"
    verify_error = ''
    v_error = "Passwords don't match"
    email_error = ''
    e_error = "That's not a valid email"
        
    if username == '':
        username_error = un_error
    if len(username) > 20 or len(username) < 3:
        username = un_error
    for i in username:
        if i == " ":
            username_error = un_error

    if password == '':
        password_error = pw_error
    if len(password) > 20 or len(password) < 3:
        password = ''
        password_error = pw_error
    for i in password:
        if i == " ":
            password = ''
            password_error = pw_error

    if verify != password:
        password = ''
        verify = ''
        verify_error = v_error

    if len(email) > 20 or len(email) < 3:
        email_error = e_error
    for i in email:
        if i == " ":
           email_error = e_error
    at_number = email.count("@")
    dot_number = email.count(".")
    if at_number != 1 or dot_number != 1:
        email_error = e_error
    if email == '':
        email_error = ''

    if not username_error and not password_error and not verify_error and not email_error:
        return "Welcome! " + username
    else:
        return render_template('form.html', title = 'Signup', username_error=username_error, password_error=password_error, 
            verify_error=verify_error, email_error=email_error, username=username, 
            password=password, verify=verify, email=email)   

app.run()







