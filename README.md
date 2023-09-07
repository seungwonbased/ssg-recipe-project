# <span id='top'> 🥙 한끼얼마 💰</span>

## 1.  👨🏽‍💻 한끼얼마 소개



한끼얼마는 **레시피를 공유하고, 레시피의 가격을 제공하는 커뮤니티**입니다.

> **한끼얼마를 통해 레시피를 공유하고, 가성비 있는 한끼 챙기세요 🥘**

> [🚀 배포 URL](http://13.124.132.111/)

## 2. 👥 팀 소개




## 3. 🗓️ 개발 기간 (23년 9월 1일 ~ 23년 9월 7일)

### 📌 일별 프로젝트 마일스톤

|일별|내용|
|---|---|
|1~7일차<br>(9/1 ~ 9/7)|- Flask 스터디|
|1일차<br>(9/1)|- 주제 선정, 기술 스택 및 협업툴 결정 (Notion, Discord)|
|3일차<br>(9/3)|- 세부 컨셉 기획, 세부 요구사항 정의|
|2~5일차<br>(9/2/ ~ 9/5)|- 필수 기능 개발|
|5일차<br>(9/5)|- 배포<br>- 개발 / 운영 환경 분리|
|5~7일차 <br>(9/5 ~ 9/7)|- 디버깅<br>- 추가 기능 구현|
|7일차<br>(9/7>|- 보고서 작성|

## 4. 🌏 개발 및 운영 환경
### ⚙️ 기술 스택

![Static Badge](https://img.shields.io/badge/Python3-3776AB?logo=Python&logoColor=%23FFFFFF)  ![Static Badge](https://img.shields.io/badge/Flask-000000?logo=Flask&logoColor=%23FFFFFF)  ![Static Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=PostgreSQL&logoColor=%23FFFFFF)  ![Static Badge](https://img.shields.io/badge/SQLite-000000?logo=SQLite&logoColor=%23FFFFFF)  ![Static Badge](https://img.shields.io/badge/AWS-FF9900?logo=Amazon%20AWS&logoColor=%23FFFFFF) 
![Static Badge](https://img.shields.io/badge/HTML5-E34F26?logo=HTML5&logoColor=%23FFFFFF)  ![Static Badge](https://img.shields.io/badge/Bootstrap-7952B3?logo=Bootstrap&logoColor=%23FFFFFF)

### ⌨️ 개발 환경

- 승원
	- OS: ![Static Badge](https://img.shields.io/badge/Mac%20OS%20Ventura-%23000000?logo=Apple&logoColor=%23FFFFFF)
	- Editor: ![Static Badge](https://img.shields.io/badge/VSCode-007ACC?logo=Visual%20Studio%20Code&logoColor=%23FFFFFF)
- 종훈
	- OS: ![Static Badge](https://img.shields.io/badge/Windows%2010-%230078D6?logo=Windows%2010&logoColor=%23FFFFFF)
	- IDE: ![Static Badge](https://img.shields.io/badge/PyCharm-%23000000?logo=PyCharm&logoColor=%23FFFFFF)

### 🏭 운영 환경

- AWS Lightsail Instance
	- 1GB RAM, 2 vCPU, 40GB SSD
- OS: ![Static Badge](https://img.shields.io/badge/Ubuntu%2020.04-%23E95420?logo=Ubuntu&logoColor=%23FFFFFF)
- DB: ![Static Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=PostgreSQL&logoColor=%23FFFFFF)

### ☎️ Communication Tool: Discord
#### 채널 구성

```
- CHAT CHANNEL
	# 라운지
	# 공지
	# 아이디어
	# 레퍼런스
	# 이슈
	# 질문
	# 파일-및-코드
- VOICE CHANNEL
	# 미팅
```
- #라운지: 자유롭게 토론
- #공지: 미팅, 일정, 회의록 공지
- #아이디어: 번뜩이는 아이디어
- #레퍼런스: 참고할만한 서비스, 자료 레퍼런스
- #이슈: 개발 및 프로젝트 진행에 있어 생기는 이슈
- #질문: 진짜 아무 질문이나
- #파일-및-코드: 파일 및 코드 공유
- #미팅: 보이스 & 페이스 미팅

## 5. ⚒️ 서비스 기능 및 특징
##




# 디렉터리 구조

```
📁 recipe-book
├──📁 app
│   ├──📁 api
│   ├──📁 static
│   ├──📁 templates
│   ├──📁 views
│   ├──📄 __init__.py
│   ├──📄 forms.py
│   └──📄 models.py
├──📁 config
│   ├──📄 __init__.py
│   ├──📄 default.py
│   ├──📄 develoment.py
│   └──📄 production.py
├──📁 logs
├──📄 .gitignore
├──📄 app.db
├──📄 requirements.txt
└──📄 README.md
```
### 📁 app
<details> <summary> 💡: Flask 애플리케이션에 관련된 디렉터리 (접기 / 펼치기) </summary> 
<!-- summary 아래 한칸 공백 두어야함 -->
- 📁 api: 공공데이터 API를 호출하는 클라이언트<br>
- 📁 static: 이미지, css, js 등의 정적 파일을 저장하는 디렉터리<br>
- 📁 templates: HTML 템플릿을 저장하는 디렉터리<br>
- 📁 views: Blueprint 파일을 저장하는 디렉터리<br>
- 📄 __init__.py: 애플리케이션 팩토리 함수가 있는 파일<br>
- 📄 forms.py: 랜더링에 필요한 HTML 코드를 생성하며 웹 애플리케이션의 입력 폼을 정의하고 필드를 추가하는 Form 클래스가 정의되어 있는 파일<br>
- 📄 models.py: 데이터를 객체에 담아 ORM을 이용하기 위한 클래스가 정의되어 있는 파일<br>
- </details>
### 📁 config
<details> <summary> 💡: 환경 파일을 저장하는 디렉터리 (접기 / 펼치기) </summary> <!-- summary 아래 한칸 공백 두어야함 -->
- 📄 __init__.py: 패키지로 인식하기 위해 생성한 파일
- 📄 default.py: 모든 환경에서 공통으로 사용할 환경 변수를 저장하는 파일
- 📄 develoment.py: 개발 환경에서 사용할 환경 변수를 저장하는 파일
- 📄 production.py: 운영 환경에서 사용할 환경 변수를 저장하는 파일 </details>
### 📁 logs
- 💡: 로그 파일을 저장하는 디렉터리, 운영 환경에서만 사용
### 📄 requirements.txt
- 💡: 가상 환경에서 설치한 라이브러리들을 파일로 내보내 다른 환경에서도 쉽게 같은 환경을 구축할 수 있게 함

## URL 
```
/ : 메인 페이지, index.html
├── /post : 게시글 Blueprint
│     ├── /list : 게시글 리스트
│     ├── /detail/<int:post_id> : 게시글 상세
│     ├── /create : 게시글 작성 (HTTP Method: GET, POST)
│     ├── /modify/<int:post_id> : 게시글 수정 (HTTP Method: GET, POST)
│     ├── /delete/<int:post_id> : 게시글 삭제
│     └── /like/<int:post_id> : 게시글 좋아요
├── /comment : 댓글 Blueprint
│     ├── /create/<int:post_id> : 댓글 생성 (HTTP Method: POST)
│     ├── /modify/<int:comment_id> : 댓글 수정 (HTTP Method: GET, POST)
│     ├── /delete/<int:comment_id> : 댓글 삭제
│     └── /like/<int:post_id>/ : 게시글 좋아요
└── /auth : 인증 Blueprint
      ├── /signup : 회원 가입 (HTTP Method: GET, POST)
      ├── /login : 로그인 (HTTP Method: GET, POST)
      └── /logout : 로그아웃
```

# 서비스 특징 및 사용 라이브러리

## Flask
- 간결함
## Application Factory Pattern
```python
# Factory Function
def create_app():
    app = Flask(__name__)
    app.config.from_envvar("APP_CONFIG_FILE")

    db.init_app(app)
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

	...

	return app
```
- 애플리케이션 객체를 Factory Function을 사용해 동적으로 생성하고 설정
- Flask 애플리케이션을 생성하고 초기화하는 디자인 패턴
	- 애플리케이션 객체를 Factory Function을 사용해 동적으로 생성하고 설정
		- 여러 개의 서로 다른 애플리케이션 인스턴스를 만들고 다른 환경(개발, 테스트 프로덕션)에서 실행할 수 있음
		- 이를 통 본 프로젝트에서 개발과 운영 환경의 설정을 다르게 함
	- 장점
		- 확장성 향상
		- 설정과 환경 관리의 용이

## Blueprint
- Flask 블루프린트는 웹 애플리케이션을 여러 개의 독립적인 모듈로 나누고, 각 모듈을 개별적으로 작업하거나 재사용할 수 있게 해줌
- 라우팅 함수의 집합
- 웹 애플리케이션을 개발할 때 코드를 더 구조화하고 관리하기 쉽게 만듬
- 장점
	1. 모듈화
		- 각 기능을 독립적인 블루프린트로 정의하여 모듈화된 코드 작성이 가능하므로 유지 보수와 확장이 용이
	2. . 라우팅 분리
		- URL 라우팅을 각 블루프린트 내에서 관리하므로 충돌을 방지하고 URL 구조를 구성하기 쉬움
	3. 코드 재사용
		- 비슷한 기능을 다른 애플리케이션에서 재사용할 수 있음

## Server-Side Rendering
- Front-end 애플리케이션 개발이 불가능해 웹 애플리케이션의 뷰를 서버에서 생성해 클라이언트에게 전달하는 방식인 SSR 사용

## Object-Relational Mapping
- 객체와 관계형 데이터베이스 간의 상호 작용을 간단하게 만들어주는 프로그래밍 기술 또는 도구
- ORM은 데이터베이스 테이블과 OOP 언어 간의 불일치를 해결하고 데이터베이스와 애플리케이션 코드 간의 상호 작용을 추상화
- Python에서는 SQLAlchemy 사용
- 장점
	1. 객체지향 코드로 비즈니스 로직에 집중 가능
	2. 재사용 및 유지보수 편리성 증가
	3. DBMS에 대한 종속성 줄어듬
- 단점
	1. ORM만으로는 서비스 구현이 어려움
	2. 프로시저(작업)가 많은 시스템에서는 장점을 취하기 어려움
- Workflow
	1. 데이터 모델 정의: 데이터베이스 테이블과 매핑될 데이터 모델(클래스)을 정의
	2. ORM 설정: ORM을 설정하여 데이터베이스 연결 정보와 데이터 모델 간의 매핑 규칙을 설정
	3. CRUD 작업: 애플리케이션 코드에서 ORM을 사용하여 데이터를 CRUD
	4. 쿼리 실행: ORM은 개발자가 작성한 ORM 코드를 기반으로 SQL 쿼리를 생성하고 데이터베이스에 전송하여 실행
	5. 결과 처리: 데이터베이스에서 반환된 결과를 객체로 변환하거나 필요한 작업을 수행
- 예시: Python code -> SQL query
```python
sub_query = db.session.query(Comment.post_id, Comment.content, User.username)   .join(User, Comment.user_id == User.id).subquery()
```
```sql
SELECT * 
FROM post_list INNER JOIN "User" ON post_list.user_id = "User".id 
LEFT OUTER JOIN sub_query ON sub_query.post_id = post_list.id 
WHERE post_list.subject ILIKE 'search_value';
```

### Flask ORM Library: SQLAlchemy
- Python을 위한 ORM 및 SQL 툴킷 라이브러리
- 데이터데이스와 상호작용하기 위한 도구 제공
- 구성 요소
	- Core: 데이터베이스와 상호작용하기 위한 기본 도구 제공
	- ORM: 데이터베이스와 Python 클래스 사이의 매핑 제공
	- SQLAlchemy: 데이터베이스 테이블을 파이썬 클래스로 정의
	- Session: 세션을 통해 데이터베이스에 대한 트랜잭션을 관리
	- Engine: 데이터베이스에 대한 모든 SQL 작업이 수행됨
	- Query: SQL 쿼리를 생성하고 실행하는 쿼리 빌더를 제공
- DB 관리 명령어
	- flask db migrate: 모델을 생성하거나 변경할 때 사용
	- flask db upgrade: 모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용

### Models.py
- Models.py 파일에 ORM을 사용해 모델을 정의했음
	- 데이터베이스 테이블과 상호작용하기 위한 클래스를 정의함
- 클래스의 각 속성은 매핑되는 테이블의 Column과 일치
- 데이터 유형과 제약 조건 또한 지정

## @Decorator
### @app.route
- Routing Function
- 애플리케이션의 URL 경로에 따라 어떤 함수가 실행될 지를 정의하는 데코레이터
- 사용자가 특정 URL을 요청할 때 해당 URL에 연결된 라우팅 함수가 실행되어 사용자에게 응답 반환

### @bp.route
- 애플리케이션에서 블루프린트 객체를 사용해 URL 경로에 따라 어떤 함수가 실행될 지를 정의하는 데 사용되는 데코레이터
- @app.route 또한 URL 경로와 함수 간의 매핑을 정의하지만, @app.route는 Flask 애플리케이션 객체('app')에 직접 라우팅 함수를 연결하는 데 사용되는 반면, @bp.route 데코레이터는 블루프린트 객체에 라우팅 함수를 연결하는 데 사용됨
	- 블루프린트는 Flask 애플리케이션을 모듈화하고 라우팅을 구조화하는 데 사용됨
	- 블루프린트를 사용한 라우팅 함수들을 관리하는 데 유용하며 모듈화, 확장 가능의 장점이 있음

## 참고: 'request' 객체
- Flask 애플리케이션에서 HTTP 요청과 관련된 정보를 처리하려면 'request' 객체를 사용
- 이 객체는 현재 요청과 관련된 다양한 정보를 제공하며 HTTP 메서드, URL, 헤더, 쿼리 문자열, 폼 데이터, JSON 데이터 및 기타 요청 데이터에 접근할 수 있도록 도와줌
- 'request' 객체를 사용해 얻을 수 있는 주요 정보
	1. **HTTP 메소드**: `request.method`를 통해 현재 요청의 HTTP 메소드를 얻을 수 있음
		- 예를 들어, GET, POST, PUT, DELETE 등의 메소드가 반환됨
	2. **URL 정보**: `request.url`은 현재 요청의 전체 URL을 나타냄
	3. **헤더 정보**: `request.headers`는 HTTP 요청 헤더의 딕셔너리를 반환
		- 예를 들어, `request.headers['User-Agent']`를 사용하여 사용자 에이전트(User-Agent) 헤더를 얻을 수 있음
	4. **쿼리 문자열**: `request.args`는 URL의 쿼리 문자열 파라미터를 딕셔너리로 반환
		- 예를 들어, `/search?query=example` URL에서 `request.args['query']`는 "example" 값을 반환
	5. **폼 데이터**: `request.form`은 POST 요청의 폼 데이터를 딕셔너리로 반환, HTML 폼에서 제출된 데이터를 처리할 때 유용
	6. **JSON 데이터**: `request.get_json()`을 사용하여 JSON 요청 본문을 파싱하고 JSON 데이터를 얻을 수 있음
	7. **파일 업로드**: 파일 업로드가 있는 POST 요청의 경우, `request.files`를 사용하여 업로드된 파일에 접근할 수 있음    
	8. **세션 정보**: `request.session`을 사용하여 현재 요청과 관련된 세션 데이터에 접근할 수 있음

## Flask Form
- Flask 애플리케이션에서 웹 폼을 쉽게 처리하기 위한 확장 라이브러리
- 웹 폼을 쉽게 생성하고, Form validation, 데이터 수집, 에러 처리 등을 할 수 있음
- CSRF(Cross-Site Request Forgery) 방지 같은 보안 기능도 내장되어 있음
	- CSRF 토큰 코드를 삽입해야 정상적으로 데이터 전송 가능
- 사용 방법
	1. FlaskForm을 상속 받는 Form 클래스를 정의
	2. View의 라우팅 함수에서 Form 인스턴스를 생성하고 사용
		- POST 요청일 때 검증 작업 등
	3. HTML 템플릿 파일에서 웹 폼을 렌더링하고 사용자에게 입력을 받음

## Paging
### Pagenation
- SQLAlchemy 라이브러리의 Pagination 객체 사용
- 게시물 리스트가 담긴 객체에 pagenate 함수 적용
	-> Pagination 객체 반환됨
- Pagenation 객체 속성

|항목|설명|예시 값|
|---|---|---|
|items|현재 페이지에 해당하는 게시물 리스트|[<Post 1>, <Post 2>, …]|
|total|게시물 전체 개수|124|
|per_page|페이지 당 보여줄 게시물 개수|10|
|page|현재 페이지 번호|7|
|iter_pages|페이지 범위|[1, 2, 3, …, 25]|
|prev_num / next num|이전 / 다음 페이지 번호|현재 페이지가 5인 경우 4 / 6|
|has_prev / has_next|이전 / 다음 페이지 존재 여부|True / False|

## 회원가입
### WTForms
- 웹에서 폼을 정의하고 검증하기 위한 라이브러리
	- 웹 폼을 쉽게 생성하고, 사용자로부터 데이터를 수집하고 검증할 수 있음
- 회원가입을 위해 FlaskForm을 상속 받아 UserCreateForm 생성
- PasswordField, EmailField을 import
	- PasswordField: 사용자의 비밀번호를 입력받을 때 이 필드를 사용하면 비밀번호 입력을 안전하게 처리하고 Validation도 할 수 있음
		- 라우팅 함수에서 generate_password_hash 함수로 암호화
	- EmailField: StringField와 동일하지만 템플릿 자동 변환으로 사용시 \<input type="email">로 변환됨

## 로그인
- FlaskForm을 상속 받아 UserLoginForm 생성
- 로그인 여부는 g 객체를 사용해 라우팅 함수에서 검증
- 로그인 라우팅 함수에서 session, g를 import
	- session
		- Flask 애플리케이션에서 사용자 데이터를 저장하고 관리, 사용자별로 고유한 데이터 저장하는 객체
		- Flask가 세션 데이터를 암호화해 보안 유지
		- 세션을 사용하면 사용자의 로그인 상태, 장바구니 내역 등의 정보를 유지하고 상태를 추적 가능
	- g
		- Flask 애플리케이션 내에서 글로벌하게 사용되는 데이터를 저장하기 위한 객체
		- 모든 요청에서 공유되는 데이터를 저장하고, 다른 함수나 뷰에서 이 데이터에 접근 가능
		- 데이터베이스 연결, 현재 사용자 정보, 로그 기록 등과 같이 여러 곳에서 사용되는 데이터를 저장할 때 유용
- 참고: Cookie와 Session
	- 쿠키와 세션은 웹 애플리케이션에서 사용자 정보를 저장하고 유지하는 데 사용되는 두 가지 다른 메커니즘
	- Cookie
		- **목적**: 쿠키는 클라이언트 측에 데이터를 저장하는 데 사용, 주로 상태 정보를 유지하거나 사용자 특정 정보를 기억하기 위해 사용
		- **작동 방식**: 서버에서 클라이언트로 작은 데이터 조각을 보내어 쿠키로 저장하고, 이후 클라이언트는 해당 쿠키를 모든 요청과 함께 서버로 다시 전송
		- **보안**: 쿠키는 클라이언트에 저장되기 때문에 보안에 취약할 수 있으며, 중요한 데이터를 저장하는 데는 부적합할 수 있음, HTTPS와 같은 보안 연결을 통해 전송되어야 함
		- **사용 사례**: 로그인 정보, 사용자 선호 설정, 장바구니 항목 등을 저장하는 데 사용
	- **Session**
		- **목적**: 세션은 서버 측에 데이터를 저장하는 데 사용, 주로 사용자 인증 및 상태 관리를 위해 사용
		- **작동 방식**: 세션은 서버에서 데이터를 유지하고, 클라이언트에는 세션 식별자(session ID)만 전송, 클라이언트가 요청을 보낼 때마다 서버는 해당 세션 ID를 사용하여 해당 세션 데이터를 가져옴
		- **보안**: 세션 데이터는 서버에 저장되기 때문에 쿠키보다 안전, 그러나 세션 ID가 유출될 경우 보안에 취약할 수 있으므로 적절한 보안 조치가 필요
		- **사용 사례**: 로그인 상태, 사용자 정보, 장바구니 내역 등을 관리하고 상태를 추적하는 데 사용