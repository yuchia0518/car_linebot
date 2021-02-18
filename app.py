# coding=UTF-8
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

# f = open('C://Users//Willy//Desktop//汽車LineBot//lineapi.txt', 'r')

line_bot_api = LineBotApi(
    '')
handler = WebhookHandler('')


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
        RankImageList = getLocalCarRankingImage()

        Carousel = TemplateSendMessage(
            alt_text='當月國產車銷量排名',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[0],
                        title=carNameList[0],
                        text='NO.1 銷量:' + soldNumList[0],
                        actions=[
                            PostbackTemplateAction(
                                label='搜尋Youtube',
                                text=carNameList[0],
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='連結2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[1],
                        title=carNameList[1],
                        text='NO.2 銷量:' + soldNumList[1],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[2],
                        title=carNameList[2],
                        text='NO.3 銷量:' + soldNumList[2],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[3],
                        title=carNameList[3],
                        text='NO.4 銷量:' + soldNumList[3],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[4],
                        title=carNameList[4],
                        text='NO.5 銷量:' + soldNumList[4],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[5],
                        title=carNameList[5],
                        text='NO.6 銷量:' + soldNumList[5],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[6],
                        title=carNameList[6],
                        text='NO.7 銷量:' + soldNumList[6],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[7],
                        title=carNameList[7],
                        text='NO.8 銷量:' + soldNumList[7],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[8],
                        title=carNameList[8],
                        text='NO.9 銷量:' + soldNumList[8],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[9],
                        title=carNameList[9],
                        text='NO.10 銷量:' + soldNumList[9],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, Carousel)
    elif event.message.text == '進口車銷售排行':
        month, carNameList, soldNumList = getImportedCarRanking()
        monthMessage = TextSendMessage(text=month)
        # line_bot_api.reply_message(event.reply_token, monthMessage)
        RankImageList = getImportedCarRankingImage()

        Carousel = TemplateSendMessage(
            alt_text='當月國產車銷量排名',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[0],
                        title=carNameList[0],
                        text='NO.1 銷量:' + soldNumList[0],
                        actions=[
                            PostbackTemplateAction(
                                label='postback1',
                                text='postback text1',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='message1',
                                text='message text1'
                            ),
                            URITemplateAction(
                                label='uri1',
                                uri='http://example.com/1'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[1],
                        title=carNameList[1],
                        text='NO.2 銷量:' + soldNumList[1],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[2],
                        title=carNameList[2],
                        text='NO.3 銷量:' + soldNumList[2],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[3],
                        title=carNameList[3],
                        text='NO.4 銷量:' + soldNumList[3],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[4],
                        title=carNameList[4],
                        text='NO.5 銷量:' + soldNumList[4],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[5],
                        title=carNameList[5],
                        text='NO.6 銷量:' + soldNumList[5],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[6],
                        title=carNameList[6],
                        text='NO.7 銷量:' + soldNumList[6],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[7],
                        title=carNameList[7],
                        text='NO.8 銷量:' + soldNumList[7],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[8],
                        title=carNameList[8],
                        text='NO.9 銷量:' + soldNumList[8],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=RankImageList[9],
                        title=carNameList[9],
                        text='NO.10 銷量:' + soldNumList[9],
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, Carousel)
    else:
        message = TextSendMessage(text='')


def getLocalCarRanking():
    url = 'https://www.kingautos.net/'
    resp = requests.get(url, headers=headers).content
    selector = etree.HTML(resp)
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
    soup = BeautifulSoup(resp, 'html.parser')
    namedivs = soup.find('div', id='imported').find_all('span', 'carName')

    solddivs = soup.find('div', id='imported').find_all('span', 'carNum')

    carList = []
    soldList = []
    monthText = selector.xpath('/html/body/div[2]/div[2]/div/div[4]/div[3]/div[5]/ul/li[1]/a/text()')

    for namediv, solddiv in zip(namedivs, solddivs):
        carList.append(namediv.text)
        soldList.append(solddiv.text)
    return monthText[0], carList, soldList


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
