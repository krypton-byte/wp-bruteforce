from bs4 import BeautifulSoup as bs
import requests
def __start__(url,username,password):
	headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0'}
	sesi=requests.Session()
	requ=sesi.get(url+'/wp-admin',headers=headers)
	pars=bs(requ.text,'html.parser')
	if ('user_login' in requ.text) and ('user_pass' in requ.text):
		data_parsing={ 	'log':username,
				'pwd':password,
				pars.find_all('input')[2]['name']:pars.find_all('input')[2]['value'],
				pars.find_all('input')[3]['name']:pars.find_all('input')[3]['value'],
				pars.find_all('input')[4]['name']:pars.find_all('input')[4]['value'],
				pars.find_all('input')[5]['name']:pars.find_all('input')[5]['value']}
		ccc=sesi.post(pars.find_all('form')[0]['action'],data=data_parsing,headers=headers,cookies=requ.cookies).text
		if '<strong>ERROR</strong>: The password you entered for the username <strong>admin</strong> is incorrect.' in ccc:
			return False
		elif 'ERROR' in ccc:
			return False
		elif 'empty' in ccc:
			return False
		elif 'incorrect' in ccc:
			return False
		elif 'login_error' in ccc:
			return False
		elif 'Unknown username. Check again or try your email address.' in ccc:
			return False
		else:
			return True
	else:
		return False