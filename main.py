from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            .error {{color: red;}}
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form action="/" method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="">
                        <span class="error">{username_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password">
                        <span class="error">{password_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password">
                        <span class="error">{verify_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="">
                        <span class="error">{email_error}</span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route('/')
def display_user_signup_form():
    return form.format(username_error='', password_error='', verify_error='', email_error='')

@app.route('/', methods=['POST'])
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
        return form.format(username_error=username_error, password_error=password_error, 
            verify_error=verify_error, email_error=email_error, username=username, 
            password=password, verify=verify, email=email)   

app.run()







