from flask import Flask, render_template, request
from userdatabase import init_userdatabase, insert_user

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

if __name__ == '__main__':
    app.run(debug=True)
