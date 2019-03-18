from bs4 import BeautifulSoup
import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

if __name__ == '__main__':
    url = 'https://www.kingautos.net/'
    browser.get(url)
    localCarString = ''
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    namedivs = soup.find('div', id='domestic').find_all('span', 'carName')
    numdivs = soup.find('div', id='domestic').find_all('span', 'carNum')
    i = 1
    mystr = ''
    for namediv, numdiv in zip(namedivs, numdivs):
        formatstr = '%d %s %s'%(i, namediv.text, numdiv.text)
        i += 1
        mystr = mystr + formatstr + '\n'
    print(mystr)


