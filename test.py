#!/usr/bin/python
# -*- coding: utf-8 -*- 
import httplib
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib

# https://www.google.co.kr/search?newwindow=1&hl=ko&site=imghp&tbm=isch&source=hp&biw=1336&bih=877&q=car&oq=car

def get_img_keyword(keyword):
	conn = httplib.HTTPSConnection('www.google.co.kr', 443)
	headers = {
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'
			, 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
			, 'referer': 'https://www.google.co.kr/'
		}
	conn.request("GET", "/search?newwindow=1&hl=ko&site=imghp&tbm=isch&source=hp&biw=1336&bih=877&q="+keyword, headers=headers)
	r1 = conn.getresponse()
	htmltext = r1.read()
	conn.close()

	# print htmltext

	img_urls = []
	formatted_images = []

	soup = BeautifulSoup(htmltext)
	results = soup.findAll("a")	

	for r in results:
		try: 
			if "imgres?imgurl" in r['href']:
				img_urls.append(r['href'])
		except:
			a=0

	for im in img_urls:
		refer_url = urlparse(str(im))
		image_f = refer_url.query.split("&")[0].replace("imgurl=", "")
		formatted_images.append(image_f)

	return formatted_images


ret = get_img_keyword("car")
print ret 
print len(ret)









