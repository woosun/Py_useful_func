'''
텔레그램 메세지 처리
텔레그램.txt파일 여부 체크 있으면 받아온 메세지를 전송한다.
'''
def tele_sand_msg(msg): 
    telegram_option = 1
    if os.path.isfile('telegram.txt') == True:     telegram_option = 1
    if telegram_option == 1:
        import telegram
        with open('telegram.txt', mode='r', encoding='UTF8') as file: t = file.read()
        token, chat_id = t.split(',')
        bot = telegram.Bot(token=token)
    msg = "지마켓:"+msg
    logger.info(msg)
    if telegram_option == 1: bot.send_message(chat_id=chat_id, text=msg)
