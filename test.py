from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from lxml import etree

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=options,
#                            executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# html = requests.get('http://www.qiushibaike.com/text/',headers=headers).content
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

headers={"User-Agent":user_agent}

if __name__ == '__main__':
    url = 'https://www.kingautos.net/'
    resp = requests.get(url, headers=headers).content
    selector = etree.HTML(resp)
    localCarString = ''
    soup = BeautifulSoup(resp, 'html.parser')
    namedivs = soup.find('div', id='domestic').find_all('span', 'carName')
    numdivs = soup.find('div', id='domestic').find_all('span', 'carNum')
    monthText = selector.xpath('/html/body/div[2]/div[2]/div/div[4]/div[3]/div[5]/ul/li[1]/a/text()')
    i = 1
    mystr = ''
    for namediv, numdiv in zip(namedivs, numdivs):
        formatstr = '%d %s %s'%(i, namediv.text, numdiv.text)
        i += 1
        mystr = mystr + formatstr + '\n'
    print(monthText[0])
    print(mystr)


