from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('PpsikGBkL6NldjaoIr6ZeFkJvQrcce8zbpFrDUpqOIl7NuX7RIVRob9DeVxZV+1TsUQvlqJ6mUG1nv2njG2O4Yxn9+mSYPofmV3X1ywk8WubSOQQil/A99S77ZxCWV97eExQtYq0wliPyGGD7ndweAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f88ac77ef47c8bd99c2607f38c13bebe')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    if event.message.text == '國產車銷售排行':
        domesticRank = getLocalCarRanking()
        message = TextSendMessage(text=domesticRank)
    elif event.message.text == '進口車銷售排行':
        message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


def getLocalCarRanking():
    url = 'https://www.kingautos.net/'
    browser.get(url)
    localCarString = ''
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    namedivs = soup.find('div', id='domestic').find_all('span', 'carName')
    numdivs = soup.find('div', id='domestic').find_all('span', 'carNum')
    i = 1
    for namediv, numdiv in zip(namedivs, numdivs):
        formatstr = '%d %s %s' % (i, namediv.text, numdiv.text)
        i += 1
        localCarString = localCarString + formatstr + '\n'
    return localCarString





import os
if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    port=os.environ['PORT']
    app.run(host='0.0.0.0', port=port)
