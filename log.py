###로그파일 만들기
#로그파일 생성하기
#현재 실행중인 파이선 파일명으로 로그파일생성되며 자동생성이 아니라 로그명령어로 어디부분 이벤트를 실행했는지 구분할떄 사용함
import logging
import logging.handlers
filenames =os.path.basename(__file__)
filenames =filenames.split('.')
log_dir = './logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
logger.setLevel(logging.DEBUG)  # DEBUG level 까지 로깅
streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)
logger.addHandler(streamhandler)
filehandler = logging.FileHandler(log_dir+'/logfile_'+filenames[0]+'.log'.format(datetime.datetime.now()), encoding='utf-8')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
## 로그파일 만들기 끝
