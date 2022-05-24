#https://wikidocs.net/155715
#step1.라이브러리 불러오기
import  requests
from  bs4  import  BeautifulSoup  as  bs
import  telegram
import  schedule
import  time
from telegram.ext import Updater
from telegram.ext import CommandHandler

bot_token  ='5366296136:AAF9B_3YXH5fAEAefJDnkAJUC08gGTY1mX8'
bot = telegram.Bot(token = bot_token)
query = '비트코인'
chat_id  =  5342881340

#step2.새로운 네이버 뉴스 기사 링크를 받아오는 함수
def  get_new_links(old_links=[]):

    # (주의) 네이버에서 키워드 검색 - 뉴스 탭 클릭 - 최신순 클릭 상태의 url
    url  = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0'

    # html 문서 받아서 파싱(parsing)
    response  =  requests.get(url)
    soup  =  bs(response.text , 'html.parser')

    # 해당 페이지의 뉴스기사 링크가 포함된 html 요소 추출
    news_titles  =  soup.select('a.news_tit')

    # 요소에서 링크만 추출해서 리스트로 저장
    list_links  = [i.attrs['href'] for  i  in  news_titles]

    # 기존의 링크와 신규 링크를 비교해서 새로운 링크만 저장
    new_links  = [link  for  link  in  list_links  if  link  not  in  old_links]

    return  new_links


#step3.새로운 네이버 뉴스 기사가 있을 때 텔레그램으로 전송하는 함수
def  send_links():
    # 함수 내에서 처리된 리스트를 함수 외부에서 참조하기 위함
    global old_links
    old_links  = []

    # 위에서 정의했던 함수 실행
    new_links  =  get_new_links(old_links)

    # 새로운 메시지가 있으면 링크 전송
    if  new_links:
        for  link  in  new_links:
            bot.sendMessage(chat_id=chat_id, text=link)

    # 없으면 패스
    else:
        pass

    # 기존 링크를 계속 축적하기 위함

    old_links +=  new_links.copy()