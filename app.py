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
from lxml import etree

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    'PpsikGBkL6NldjaoIr6ZeFkJvQrcce8zbpFrDUpqOIl7NuX7RIVRob9DeVxZV+1TsUQvlqJ6mUG1nv2njG2O4Yxn9+mSYPofmV3X1ywk8WubSOQQil/A99S77ZxCWV97eExQtYq0wliPyGGD7ndweAdB04t89/1O/w1cDnyilFU=')
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


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

headers = {"User-Agent": user_agent}


# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=options,
#                            executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    if event.message.text == '國產車銷售排行':
        month, carNameList, soldNumList = getLocalCarRanking()
        monthMessage = TextSendMessage(text=month)
        # line_bot_api.reply_message(event.reply_token, monthMessage)
        localRankImageList = getLocalCarRankingImage()

        Image_Carousel = TemplateSendMessage(
            alt_text='當月國產車銷量排名',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url=localRankImageList[0],
                        action=PostbackTemplateAction(
                            label=carNameList[0] + '\n' + soldNumList[0],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[1],
                        action=PostbackTemplateAction(
                            label=carNameList[1] + '\n' + soldNumList[1],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[2],
                        action=PostbackTemplateAction(
                            label=carNameList[2] + '\n' + soldNumList[2],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[3],
                        action=PostbackTemplateAction(
                            label=carNameList[3] + '\n' + soldNumList[3],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[4],
                        action=PostbackTemplateAction(
                            label=carNameList[4] + '\n' + soldNumList[4],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[5],
                        action=PostbackTemplateAction(
                            label=carNameList[5] + '\n' + soldNumList[5],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[6],
                        action=PostbackTemplateAction(
                            label=carNameList[6] + '\n' + soldNumList[6],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[7],
                        action=PostbackTemplateAction(
                            label=carNameList[7] + '\n' + soldNumList[7],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[8],
                        action=PostbackTemplateAction(
                            label=carNameList[8] + '\n' + soldNumList[8],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url=localRankImageList[9],
                        action=PostbackTemplateAction(
                            label=carNameList[9] + '\n' + soldNumList[9],
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    )

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, Image_Carousel)
    elif event.message.text == '進口車銷售排行':
        month, importedRank = getLocalCarRanking()

        message = TextSendMessage(text=month + "/n" + importedRank)
    else:
        message = TextSendMessage(text='B嘴')


def getLocalCarRanking():
    url = 'https://www.kingautos.net/'
    resp = requests.get(url, headers=headers).content
    selector = etree.HTML(resp)
    localCarString = ''
    soup = BeautifulSoup(resp, 'html.parser')
    namedivs = soup.find('div', id='domestic').find_all('span', 'carName')

    solddivs = soup.find('div', id='domestic').find_all('span', 'carNum')

    carList = []
    soldList = []
    monthText = selector.xpath('/html/body/div[2]/div[2]/div/div[4]/div[3]/div[5]/ul/li[1]/a/text()')

    for namediv, solddiv in zip(namedivs, solddivs):
        carList.append(namediv.text)
        soldList.append(solddiv.text)
    return monthText[0], carList, soldList


def getLocalCarRankingImage():  # 得到國產車排名的照片
    url = 'https://www.kingautos.net/'
    resp = requests.get(url, headers=headers).content
    soup = BeautifulSoup(resp, 'html.parser')
    imgurls = soup.find('div', id='domestic').find_all('img')
    i = 1
    imglist = []
    for url in imgurls:
        if str(url).find('http') == -1:
            imgurl = url['src'].split('-')[0]
            imglist.append('https:' + imgurl + '.jpg')
        else:
            imgurl = url['src'].split('-')[0]
            imglist.append(imgurl + '.jpg')

    return imglist


def getImportedCarRanking():
    url = 'https://www.kingautos.net/'
    resp = requests.get(url, headers=headers).content
    selector = etree.HTML(resp)
    importedCarString = ''
    soup = BeautifulSoup(resp, 'html.parser')
    namedivs = soup.find('div', id='domestic').find_all('span', 'carName')
    numdivs = soup.find('div', id='domestic').find_all('span', 'carNum')
    monthText = selector.xpath('/html/body/div[2]/div[2]/div/div[4]/div[3]/div[5]/ul/li[1]/a/text()')
    i = 1
    for namediv, numdiv in zip(namedivs, numdivs):
        formatstr = '%d %s %s' % (i, namediv.text, numdiv.text)
        i += 1
        importedCarString = importedCarString + formatstr + '\n'
    print(monthText[0])
    print(importedCarString)
    return monthText[0], importedCarString


def getImportedCarRankingImage():  # 得到進口車排名的照片
    url = 'https://www.kingautos.net/'
    resp = requests.get(url, headers=headers).content
    soup = BeautifulSoup(resp, 'html.parser')
    imgurls = soup.find('div', id='imported').find_all('img')
    i = 1
    imglist = []
    for url in imgurls:
        if str(url).find('http') == -1:
            imgurl = url['src'].split('-')[0]
            imglist.append('https:' + imgurl + '.jpg')
        else:
            imgurl = url['src'].split('-')[0]
            imglist.append(imgurl + '.jpg')

    return imglist


import os

if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    port = os.environ['PORT']
    app.run(host='0.0.0.0', port=port)
