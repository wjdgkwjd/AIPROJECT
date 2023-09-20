import urllib.request

from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4")

soup = BeautifulSoup(html, "html.parser")

img_src=soup.find_all('img')

for i in range(10):

  urllib.request.urlretrieve(img_src[i]['src'],f"image-{i}.jpg")