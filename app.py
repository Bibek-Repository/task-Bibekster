from flask import Flask, render_template, request, redirect, url_for
from userdatabase import init_userdatabase, insert_user, check_user_in_database

app = Flask(__name__)

# Initialize the database
init_userdatabase()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form2', methods=['POST'])
def submit_form2():
    # Retrieve the form data
    username = request.form['username']
    password = request.form['password']

    # Insert data into the database
    try:
        insert_user(username, password)
        return 'Form submitted successfully! Username and password stored in the database.'
    except Exception as e:
        return f'An error occurred: {str(e)}'
    
@app.route('/submit_form1', methods=['POST'])
def submit_form1():
    # Retrieve the form data
    username = request.form['username']
    password = request.form['password']

    
    # Validate the credentials
    if check_user_in_database(username, password):
        # Redirect to the user page with the username as a parameter
        return redirect(url_for('userpage', username=username))
    else:
        return 'Invalid username or password. Please try again.', 401

@app.route('/userpage/<username>')
def userpage(username):
    # Render the user page
    return render_template('userpage.html', username=username)
    

if __name__ == '__main__':
    app.run(debug=True)
