import urllib

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from lxml import etree

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=options,
#                            executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# html = requests.get('http://www.qiushibaike.com/text/',headers=headers).content
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

headers = {"User-Agent": user_agent}

if __name__ == '__main__':
    resp = requests.get('https://www.youtube.com/user/tw8891/search?query=rav4')
    soup = BeautifulSoup(resp.text,'html5lib')
    divs = soup.find_all('a')
    for div in divs:
        if(div['title']):
            print('')
        else:
            print(div['title'])



    # f = open('C://Users//Willy//Desktop//汽車LineBot//lineapi.txt', 'r')
    #
    # print(f.readline())
    # print(f.readline())
    # url = 'https://www.kingautos.net/'
    # resp = requests.get(url, headers=headers).content
    # selector = etree.HTML(resp)
    # localCarString = ''
    # soup = BeautifulSoup(resp, 'html.parser')
    # namedivs = soup.find('div', id='domestic').find_all('span', 'carName')
    # numdivs = soup.find('div', id='domestic').find_all('span', 'carNum')
    # monthText = selector.xpath('/html/body/div[2]/div[2]/div/div[4]/div[3]/div[5]/ul/li[1]/a/text()')
    # imgurls = soup.find('div', id='domestic').find_all('img')
    # i = 1
    # for namediv, numdiv in zip(namedivs, numdivs):
    #     formatstr = '%d %s %s' % (i, namediv.text, numdiv.text)
    #     i += 1
    #     localCarString = localCarString + formatstr + '\n'
    # print(monthText[0])
    # print(localCarString)

    # url = 'https://www.kingautos.net/'
    # resp = requests.get(url, headers=headers).content
    # selector = etree.HTML(resp)
    # localCarString = ''
    # soup = BeautifulSoup(resp, 'html.parser')
    # namedivs = soup.find('div', id='domestic').find_all('span', 'carName')
    #
    # solddivs = soup.find('div', id='domestic').find_all('span', 'carNum')
    #
    # carList = []
    # soldList = []
    # monthText = selector.xpath('/html/body/div[2]/div[2]/div/div[4]/div[3]/div[5]/ul/li[1]/a/text()')
    #
    # for namediv, solddiv in zip(namedivs, solddivs):
    #     carList.append(namediv.text)
    #     soldList.append(solddiv.text)
    # print(monthText[0])
    # print(carList[5])
