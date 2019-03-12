from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    port=os.environ['PORT']
    app.run(host='127.0.0.1', port=port)
