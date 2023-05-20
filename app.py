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
			cursor.execute(f"UPDATE accounts SET logins = '{addLogin(account['logins'])}' WHERE id = {account['id']}")
			mysql.connection.commit()
			cursor.execute(f"SELECT * FROM ml WHERE id = {account['id']}")
			ml = cursor.fetchone()
			session['qa'] = f"{ml ['qa']:02}"
			ans = ml ['qa']
			session['ans'] = "......." if ans is None else ans 
			return render_template('redirect.html', name=account ['name'])
		else:
			msg = '登入資料錯誤!'
	return render_template('login.html', msg=msg)

QS = [ ]

def unzip (ans):
    

@app.route('/')
@app.route('/answers', methods=['GET', 'POST'])
def answers():
	if 'loggedin' in session:
		if request.method == 'POST':
			c = 0
			for i in range (1, 6):
				a = request.form.get (f'I{i}')
				session ['ans'][c] = '.' if a is None else a [-1]
				c += 1
			for i in [ 'II', 'III' ]:
				for j in range (1, 3):
					a = request.form.get (f'{i}{j}')
					session ['ans'][c] = '.' if a is None else a [-1]
					c += 1
			mysql.connection.cursor(MySQLdb.cursors.DictCursor).execute(f"UPDATE ml SET ans = '{session ['ans']}' WHERE id = {session['account']['id']}")
			mysql.connection.commit()
		return render_template('answers.html', ans = unzip (session ['ans']), name = session ['account']['name'])
	else:
		return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('account', None)
    session.pop('qa', None)
    session.pop('ans', None)
    return redirect (url_for('login'))

@app.route("/questions")
def questions():
    return render_template('questions.html', pdf = url_for ('static', filename=f"qs/{ session ['qa'] }q.pdf"), name = session ['account']['name'])

if __name__ == "__main__":
	app.run(host="localhost", port=int("5000"))
