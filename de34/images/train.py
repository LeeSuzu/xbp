import requests
from bs4 import BeautifulSoup

def scrape_jr_tokaido_yokohama_schedule():
    url = "https://www.jreast.co.jp/timetable/list.html"

    # HTTP GETリクエストを送信
    response = requests.get(url)

    # HTMLの解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # JR東海道線の横浜駅着の時刻表部分のセレクターを特定
    yokohama_schedule = soup.find("div", {"id": "line03_yokohama"})

    # 時刻表のテキストを取得
    schedule_text = yokohama_schedule.get_text()

    return schedule_text

# JR東海道線の横浜駅着の時刻表を取得して表示
jr_tokaido_yokohama_schedule = scrape_jr_tokaido_yokohama_schedule()
print(jr_tokaido_yokohama_schedule)
