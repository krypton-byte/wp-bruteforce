from markupsafe import escape
from flask import *
import sqlite3,os
fl=Flask(__name__)
fl.secret_key=b'_5#y2L"F4Q8z\n\xec]/'
@fl.route('/login', methods=['GET','POST'])
def login():
	try:
		if 'email' in session and 'password' in session:
			return verif(session['email'],session['password']) 
		elif request.method == 'POST':
			return verif(request.form['email'],request.form['password'])
		else:
				return render_template('login.html')
	except:
		return 'isinya yg bener kampank'
@fl.route('/register',methods=['GET','POST'])
def regist():
	try:
		if request.method == 'POST':
			session['email'] = request.form['email']
			session['password'] = request.form['password']
			ss=sqlite3.connect('dabes.db')
			ss.execute("INSERT INTO LOGIN ( NAMA, EMAIL, PASSWORD, ALAMAT, GENDER, SEKOLAH, NOWA, UMUR, STATUS ) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(request.form['nama'],request.form['email'],request.form['password'],request.form['alamat'],request.form['gender'],request.form['sekolah'],request.form['nowa'],request.form['umur'],request.form['status']))
			ss.commit()
			ss.close()
			return redirect(url_for('login'))
		else:
			return render_template('index.html')
	except:
		return 'isinya yg bener kampank'
@fl.route('/', methods=['GET','POST'])
def index():
	if ('username' in session) and ('password' in session):
		return verif(session['username'],session['password'])
	else:
		return redirect(url_for('login'))

def verif(email,password):
	nn=sqlite3.connect('dabes.db')
	nm=nn.execute('SELECT NAMA, EMAIL, PASSWORD, ALAMAT, GENDER, SEKOLAH, NOWA, UMUR, STATUS FROM LOGIN')
	for x in nm:
		if x[1] == email and x[2] == password:
			return 'NAMA : %s<br>EMAIL : %s <br>PASSWORD : %s<br>ALAMAT : %s<br>GENDER : %s<br>SEKOLAH : %s<br>NO-WA : %s<br>UMUR : %s<br>STATUS : %s'%(escape(x[0]),escape(x[1]),escape(x[2]),escape(x[3]),escape(x[4]),escape(x[5]),escape(x[6]),escape(x[7]),escape(x[8]))
		else:
			return '<script>alert("you are not logged in")</script>'
@fl.route('/logout', methods=['GET','POST'])
def logout():
	try:
		session.pop('username',None)
		session.pop('password',None)
		return 'session removed'
	except:
		return 'kenapa log out akun aja gk ada'
@fl.errorhandler(404)
def not_found(error):
	return '<h1> Oops! laman tidak tersedia</h1>'

if __name__ == '__main__':
	fl.run(host='127.0.0.1',port=int(os.environ.get('PORT',5000)),debug=True)
