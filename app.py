# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re, getpass
from flask_socketio import SocketIO
from flask_login import logout_user

app = Flask(__name__)

app.secret_key = 'eltonhuang'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = getpass.getpass ('mysql password: ')
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)
# socketio = SocketIO(app)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		id = request.form['username']
		pw = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute(
			'SELECT * FROM accounts WHERE id = % s \
			AND pw = % s', (id, pw, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['name']
			return render_template('index.html', msg=f"{session['username']}，今天繼續加油喔！")
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/index")
def index():
	if 'loggedin' in session:
		return render_template("index.html", msg=f"{session['username']}，今天繼續加油喔！")
	return redirect(url_for('login'))


@app.route("/display")
def display():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE id = % s',
					(session['id'], ))
		account = cursor.fetchone()
		return render_template("display.html", account=account)
	return redirect(url_for('login'))


@app.route("/update", methods=['GET', 'POST'])
def update():
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
		return render_template("update.html", msg=msg)
	return redirect(url_for('login'))

# @socketio.on('disconnect')
# def disconnect_user():
#     logout_user()
#     logout()
    
if __name__ == "__main__":
    # socketio.run(app)
	app.run(host="localhost", port=int("5000"))
