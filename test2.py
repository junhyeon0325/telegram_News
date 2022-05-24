import test1 as a

#step1.telegram 패키지의 Updater, CommandHandler 모듈 import
from telegram.ext import Updater
from telegram.ext import CommandHandler

chat_id  =  5342881340
#step2.Updater(유저의 입력을 계속 모니터링하는 역할), Dispatcher
updater = Updater(token='5366296136:AAF9B_3YXH5fAEAefJDnkAJUC08gGTY1mX8', use_context=True)
dispatcher = updater.dispatcher

#step3./start 명령어가 입력되었을 때의 함수 정의
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="비트코인과 관련된 뉴스 기사들입니다.")
    a.send_links()

#step4.위에서 정의한 함수를 실행할 CommandHandler 정의
start_handler = CommandHandler(a.query, start) #('명렁어',명령 함수)

#step5.Dispatcher에 Handler를 추가
dispatcher.add_handler(start_handler)

#step6.Updater 실시간 입력 모니터링 시작(polling 개념)
updater.start_polling()