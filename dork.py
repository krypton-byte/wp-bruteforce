import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
def __start__(payload,waktu,halaman):
	USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0'
	MOBILE_USER_AGENT = 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'
	URL = 'https://google.com/search'
	headers = {'User-Agent': USER_AGENT}
	hasil=[]
	for x in range(0, int(halaman)):
		query={'q':payload,'start':waktu,'num':halaman}
		resp = requests.get(URL, params=query, headers=headers)
		if resp.status_code == 200:
			soup = BeautifulSoup(resp.content, 'html.parser')
		for z in soup.find_all('div', class_='r'):
			alamat = z.find_all('a')
		if alamat:
			link = alamat[0]['href']
			domain = urlparse(link)
			hasil.append(domain.scheme + '://' + domain.netloc+'\n')
	return ''.join(hasil)
