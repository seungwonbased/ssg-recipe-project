from logging.config import dictConfig
from config.default import *
from dotenv import load_dotenv


load_dotenv(os.path.join(BASE_DIR, '.env'))


SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'Zb3\x81\xdb\xf1\xd9\xd7-Knb\x8eB\xa5\x18'


"""
- dictConfig
1. version
    - 1로 고정, 아니면 ValueError 발생
    - logging 모듈 업그레이드해도 현재 설정 보장
2. formatters
    - 로그를 출력할 형식 정의
    - default 포매터 등록
        - asctime: 현재 시간
        - levelname: 로그의 레벨
        - module: 로그를 호출한 모듈명
        - massage: 출력 내용
3. handlers
    - 로그를 출력하는 방법 정의
    - file 핸들러 등록
        - level: 출력 로그 레벨
        - class: 로그 핸들러 클래스, 로그가 너무 커져서 디스크가 꽉 차는 것을 방지
        - filename: 로그 파일명
        - maxBytes: 로그 파일 크기
        - backupCount: 로그 파일 개수
        - formatter: 포매터
4. root
    - 최상위 로거
        - level: 로그 레벨
        - handlers: 로그 핸들러
"""
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/ssgrecipe.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})
