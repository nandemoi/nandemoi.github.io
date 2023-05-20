# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re, getpass
from datetime import date

app = Flask(__name__)

app.secret_key = 'eltonhuang'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = getpass.getpass ('mysql password: ')
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

def addLogin (logins):
    today = date.today().strftime("%m/%d")
    if logins is None:
        return today
    else:
        if re.search (rf"{re.escape(today)}$", logins):
            return logins
        else:
            return f"{logins}, {today}"

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(f"SELECT * FROM accounts WHERE id = {request.form['username']} AND pw = {request.form['password']}")
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['account'] = account
            logins = addLogin(account['logins'])
            cursor.execute(f"UPDATE accounts SET logins = '{logins}' WHERE id = {account['id']}")
            mysql.connection.commit()
            cursor.execute(f"SELECT * FROM ml WHERE id = {account['id']}")
            ml = cursor.fetchone()
            session['qa'] = f"{ml ['qa']:02}"
            return render_template('index.html', name=account['name'], logins=logins)
        else:
            msg = '登入資料錯誤!'
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('account', None)
    session.pop('qa', None)
    return redirect(url_for('login'))

@app.route('/display_pdf')
def display_pdf():
    return send_file (url_for ('static', filename=f"qs/{ session ['qa'] }q.pdf"), mimetype='application/pdf')
    
@app.route("/questions")
def questions():
    if 'loggedin' in session:
        return """
        <script>
            window.open('/display_pdf', f"{session ['account']['name']}題目");
        </script>
        """
    else:
        return redirect(url_for('login'))

@app.route("/answers", methods=['GET', 'POST'])
def answers():
	msg = ''
	if 'loggedin' in session:
		if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
			username = request.form['username']
			password = request.form['password']
			email = request.form['email']
			organisation = request.form['organisation']
			address = request.form['address']
			city = request.form['city']
			state = request.form['state']
			country = request.form['country']
			postalcode = request.form['postalcode']
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute(
				'SELECT * FROM accounts WHERE username = % s',
					(username, ))
			account = cursor.fetchone()
			if account:
				msg = 'Account already exists !'
			elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				msg = 'Invalid email address !'
			elif not re.match(r'[A-Za-z0-9]+', username):
				msg = 'name must contain only characters and numbers !'
			else:
				cursor.execute('UPDATE accounts SET username =% s,\
				password =% s, email =% s, organisation =% s, \
				address =% s, city =% s, state =% s, \
				country =% s, postalcode =% s WHERE id =% s', (
					username, password, email, organisation,
				address, city, state, country, postalcode,
				(session['id'], ), ))
				mysql.connection.commit()
				msg = 'You have successfully updated !'
		elif request.method == 'POST':
			msg = 'Please fill out the form !'
		return render_template("answers.html", msg=msg)
	return redirect(url_for('login'))

if __name__ == "__main__":
	app.run(host="localhost", port=int("5000"))
