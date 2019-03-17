import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
import urllib
import os
import requests
import datetime

# base_url = 'https://twitter.com/39saku_chan/media'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

MEMBER_URL = [
    'https://twitter.com/39saku_chan/media',
    'https://twitter.com/shiromiru36/media',
    'https://twitter.com/mariyagiii310/media',
    'https://twitter.com/katorena_710/media',
    'https://twitter.com/nako_yabuki_75/media',
    'https://twitter.com/mionnn_48/media',
    'https://twitter.com/okadanana_1107/media',

    'https://twitter.com/mak0_k0jima/media',
    'https://twitter.com/yuka_ippaiwarae/media',
    'https://twitter.com/Nana_Owada728/media',
    'https://twitter.com/rika_nakai823/media',
    'https://twitter.com/miku_monmon3939/media',
    'https://twitter.com/maho_yamaguchi/media',
    'https://twitter.com/o_megu1112/media',
    'https://twitter.com/yuiyui_maromaro/media',
    'https://twitter.com/M_Hana119/media',
    'https://twitter.com/yui_hiwata430/media',
    'https://twitter.com/912_komiharu/media',
    'https://twitter.com/yuna_obata48/media',
    'https://twitter.com/macyacyarin/media',
    'https://twitter.com/erii_20031027/media',
    'https://twitter.com/48moeka_yahagi/media',
    'https://twitter.com/Berin_official/media',
    'https://twitter.com/katominami0115/media',
    'https://twitter.com/AKB48K5/media',
    'https://twitter.com/hinata_homma/media',
    'https://twitter.com/Kuranoo_Narumi_/media',
    'https://twitter.com/__cho__kurena8/media',
    'https://twitter.com/s_snowgirl_n/media',
    'https://twitter.com/oguma_tsugumi/media',
    'https://twitter.com/nanaseworld_7/media',
    'https://twitter.com/rei_1025_48/media',
    'https://twitter.com/MizukiYamauchi/media',
    'https://twitter.com/ayutaro_ngt48/media',
    'https://twitter.com/piyomi48/media',
    'https://twitter.com/official_seiji/media',
    'https://twitter.com/H_KANNA_0203',
    'https://twitter.com/Yuno__official',
    'https://twitter.com/nagasawa_marina',
    'https://twitter.com/_aeri_yokoshima']


def get_web_page(url):
    resp = requests.get(
        url=url,

    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def parse(url):
    browser.get(url)
    time.sleep(0.5)

    for _ in range(2):
        browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

    soup = BeautifulSoup(browser.page_source, 'html5lib')
    times = soup.find_all('span', '_timestamp')
    day_count_list = []
    for t in times:
        post_time = datetime.datetime.fromtimestamp(int(t['data-time'])).strftime("%Y-%m-%d")
        post_year = int(post_time.split('-')[0])
        post_month = int(post_time.split('-')[1])
        post_day = int(post_time.split('-')[2])
        post_time_format = datetime.datetime(post_year, post_month, post_day)

        now = datetime.datetime.now().strftime("%Y-%m-%d")
        nowyear = int(now.split('-')[0])
        nowmonth = int(now.split('-')[1])
        nowday = int(now.split('-')[2])
        now_format = datetime.datetime(nowyear, nowmonth, nowday)
        day_count = (now_format - post_time_format).days
        day_count_list.append(day_count)
        # print('差幾天', day_count)

    print('最後發文距離今天差:', day_count_list[0], '天')

    tweets = soup.find_all("img", {'src': re.compile('https://pbs.twimg.com/media.*')})
    img_urls = []
    # for tweet in tweets:
    #     img_urls.append(tweet['src'])
    #     print(tweet['src'])

    for idx, val in enumerate(tweets):
        # print('idx',idx)
        if abs(day_count_list[idx]) > 7:  # 此處控制要提取多久以前的照片(預設值一個禮拜(7天))
            break
        else:
            img_urls.append(val['src'])
            print(val['src'])

    return img_urls


def save(img_urls, member):
    if img_urls:
        try:
            for img_url in img_urls:
                fname = img_url.split('/')[-1]
                print(fname)

                if '39saku_chan' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\宮脇咲良', fname))
                elif 'shiromiru36' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\白間美瑠', fname))
                elif 'mariyagiii310' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\永尾まりあ', fname))
                elif 'katorena_710' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\加藤玲奈', fname))
                elif 'nako_yabuki_75' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\矢吹奈子', fname))
                elif 'mionnn_48' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\向井地美音', fname))
                elif 'okadanana_1107' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\岡田奈々', fname))
                elif 'mak0_k0jima' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\小嶋真子', fname))
                elif 'Nana_Owada728' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\大和田南那', fname))
                elif 'rika_nakai823' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\中井りか', fname))
                elif 'miku_monmon3939' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\田中美久', fname))
                elif 'maho_yamaguchi' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\山口真帆', fname))
                elif 'o_megu1112' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\谷口めぐ', fname))
                elif 'yuiyui_maromaro' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\小栗有以', fname))
                elif 'M_Hana119' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\松岡はな', fname))
                elif 'yui_hiwata430' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\樋渡結依', fname))
                elif '912_komiharu' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\込山榛香', fname))
                elif 'yuna_obata48' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\小畑優奈', fname))
                elif 'macyacyarin' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\馬嘉伶', fname))
                elif 'erii_20031027' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\千葉恵里', fname))
                elif '48moeka_yahagi' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\矢作萌夏', fname))
                elif 'Berin_official' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\岡部麟', fname))
                elif 'katominami0115' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\加藤美南', fname))
                elif 'AKB48K5' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\久保怜音', fname))
                elif 'hinata_homma' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\本間日陽', fname))
                elif 'Kuranoo_Narumi_' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\倉野尾成美', fname))
                elif '__cho__kurena8' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\長久玲奈', fname))
                elif 's_snowgirl_n' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\坂口渚沙', fname))
                elif 'oguma_tsugumi' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\小熊倫実', fname))
                elif 'nanaseworld_7' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\吉川七瀬', fname))
                elif 'rei_1025_48' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\西川怜', fname))
                elif 'MizukiYamauchi' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\山内瑞葵', fname))
                elif 'ayutaro_ngt48' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\中村歩加', fname))
                elif 'piyomi48' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\奈良未遥', fname))
                elif 'official_seiji' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\清司麗菜', fname))
                elif 'aina_k_26' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\日下部愛菜', fname))
                elif 'H_KANNA_0203' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\橋本環奈', fname))
                elif 'Yuno__official' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\大原優乃', fname))
                elif 'nagasawa_marina' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\長澤茉里奈', fname))
                elif '_aeri_yokoshima' in member:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48\横島亜衿', fname))
                else:
                    urllib.request.urlretrieve(img_url, os.path.join('D:\IMAGE\AKB48', fname))


        except Exception as e:
            print(e)


if __name__ == '__main__':
    for member_url in MEMBER_URL:
        current_page = get_web_page(member_url)
        print('目前解析網址:  ', member_url)

        mem_account_name = str(member_url).split("/")
        print('メンバー： ', mem_account_name[3])

        if current_page:
            img_urls = parse(member_url)
            # print(mem_account_name[3])
            save(img_urls, mem_account_name[3])

    browser.quit()
