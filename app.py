# Store this code in 'app.py' file
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, send_file
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

def addLogin (logins, mac):
    today = date.today().strftime(f"%m/%d{'' if mac is None else f' ({mac})'}")
    if logins is None:
        return today
    else:
        if re.search (rf"{re.escape(today)}$", logins):
            return logins
        else:
            return f"{logins}, {today}"

def getDbCrsr ():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute(f"SELECT * FROM accounts WHERE id = {request.form['username']} AND pw = {request.form['password']}")
	return cursor

def procLogin (account, cursor, mac):
	session['loggedin'] = True
	session['account'] = account
	cursor.execute(f"UPDATE accounts SET logins = '{addLogin(account['logins'], mac)}' WHERE id = {account['id']}")
	mysql.connection.commit()
	cursor.execute(f"SELECT * FROM ml WHERE id = {account['id']}")
	ml = cursor.fetchone()
	session['qa'] = f"{ml ['qa']:02}"
	session['ans'] = "........." if ml ['ans'] is None else ml ['ans'] # unzip ("........." if ml ['ans'] is None else ml ['ans'])

@app.route('/')
@app.route('/weblogin', methods=['GET', 'POST'])
def weblogin():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		cursor = getDbCrsr()
		account = cursor.fetchone()
		if account:
			procLogin (account, cursor, None)
			return redirect (url_for ('answers'))
		else:
			msg = '登入資料錯誤！請重新輸入...'
	return render_template('login.html', msg=msg)

@app.route('/applogin', methods=['GET', 'POST'])
def applogin():
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		cursor = getDbCrsr()
		account = cursor.fetchone()
		if account:
			procLogin (account, cursor, request.form ['mac'])
			return jsonify ({ "name": session ['account']['name'] })
		else:
			return jsonify ({ "name": None })
	return None

QS = [ 'I1', 'I2', 'I3', 'I4', 'I5', 'II1', 'II2', 'III1', 'III2' ]
ps = [ 1, 1, 1, 1, 1, 2, 3, 2, 3 ]

def unzip (ans):
	ansd = {}
	for a, q in zip (ans, QS):
		ansd [q] = a
	return ansd

def zipit (ansd):
	ans = ""
	for q in QS:
		ans += ansd [q]
	return ans

@app.route('/answers', methods=['GET', 'POST'])
def answers():
	if 'loggedin' in session:
		if request.method == 'POST':
			anss = ""
			for q in QS:
				a = request.form.get (q)
				anss += '.' if a is None else a [-1]
			session ['ans'] = anss
			mysql.connection.cursor(MySQLdb.cursors.DictCursor).execute(f"UPDATE ml SET ans = '{anss}' WHERE id = {session['account']['id']}")
			mysql.connection.commit()
			with open (f"ss/{session['qa']}t.txt", 'r') as f:
				sols = f.read ()
			# print (anss)
			# print (sols)
			chks = ''.join ([ '✅' if a == s else '❌' for a, s in zip (anss, sols) ])
			# print (chks)
			ptss = sum ([ps [i] if chks [i] == '✅' else 0 for i in range (len(chks))])
			return render_template('answers.html', pts = ptss, chk = chks,     pdf = url_for ('static', filename=f"qs/{ session ['qa'] }tstr.pdf"), ans = anss, name = f"{session ['account']['name']}已交卷")
		else:
			return render_template('answers.html', pts = None, chk = ['　']*9, pdf = url_for ('static', filename=f"qs/{ session ['qa'] }tstr.pdf"), ans = session ['ans'], name = f"{session ['account']['name']}作答")
	else:
		return redirect(url_for('weblogin'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('account', None)
    session.pop('qa', None)
    session.pop('ans', None)
    return redirect (url_for('login'))

if __name__ == "__main__":
	app.run(host="localhost", port=int("4000"))
