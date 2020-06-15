import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import io

# url = "https://www.youtube.com/watch?v=ZLL6GZwqNgA"
# url = "https://www.youtube.com/watch?v=RT931wkVLlw"
url = 'https://www.youtube.com/watch?v=RHNWiq-Bd9s&list=PLaAVDbMg_XArcet5lwcRo12Fh9JrGKydh&index=274'
# url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# text = soup.find_all('meta')
# text = soup.find_all('meta',attrs={'property':'og:description'})
# text1 = soup.find('p',attrs={'id':'eow-description'})
# print(text1.text)
# text2 = soup.find('span',class_='watch-title')
# print(text2.text)
# with io.open("Output3.txt",'w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# text = soup.find('strong',attrs={'class':'watch-time-text'})
text = soup.find('button',attrs={'class':'like-button-renderer-like-button'}).next_element
# text = soup.find('button.span',attrs={'class':'yt-uix-button-content'})
print(text.text)

# import urllib.request
# import json
# import urllib
# import pprint

# #change to yours VideoID or change url inparams
# VideoID = "ZLL6GZwqNgA" 

# params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
# url = "https://www.youtube.com/oembed"
# query_string = urllib.parse.urlencode(params)
# url = url + "?" + query_string

# with urllib.request.urlopen(url) as response:
#     response_text = response.read()
#     data = json.loads(response_text.decode())
#     pprint.pprint(data)
#     # print(data['title'])
#     # print(data)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import io

# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
# driver = webdriver.Firefox(executable_path=r'C:\Users\razexzzz\Documents\geckodriver-v0.26.0-win64\geckodriver.exe',options=options)
# driver.get('https://www.youtube.com/watch?v=ZLL6GZwqNgA')
# # text_file = open("output.txt","w")
# # text_file.write(driver.page_source)
# # text_file.close()
# # print(driver.find_element_by_xpath("//meta[@name='title']"))
# # print(driver.find_elements_by_tag_name('meta'))
# page_source = driver.page_source
# # fileW = open("Output.txt",'w')
# # fileW.write(page_source)
# # fileW.close()
# with io.open("Output.txt",'w',encoding='utf-8') as f:
#     f.write(page_source)
# soup = BeautifulSoup(page_source, 'html.parser')
# with io.open("Output2.txt",'w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# # text = soup.find_all('meta')
# # print(text)