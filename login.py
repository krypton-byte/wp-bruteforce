from bs4 import BeautifulSoup as bs
import requests
def __start__(url,username,password):
	headers={
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'en-us,en;q=0.5',
		'Cache-Control':'no-cache'
		}
	sesi=requests.Session()
	requ=sesi.get('%s/wp-admin'%(str(url)),headers=headers)
	pars=bs(requ.text,'html.parser')
	if ('user_login' in requ.text) and ('user_pass' in requ.text):
		data_parsing={
				'log':username,
				'pwd':password,
				pars.find_all('input')[2]['name']:pars.find_all('input')[2]['value'],
				pars.find_all('input')[3]['name']:pars.find_all('input')[3]['value'],
				pars.find_all('input')[4]['name']:pars.find_all('input')[4]['value'],
				pars.find_all('input')[5]['name']:pars.find_all('input')[5]['value']
				}

		ccc=sesi.post(pars.find_all('form')[0]['action'],data=data_parsing,headers=headers,cookies=requ.cookies).text
		if 'wordpress_logged_in' in ccc.lower():
			return True
		else:
			return False
	else:
		return False
