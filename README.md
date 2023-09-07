# <span id='top'> 🥙 한끼얼마 Report💰</span>

## 1.  👨🏽‍💻 한끼얼마 소개

![main_page](https://github.com/seungwonbased/ssg-recipe-project/blob/main/main_page.png)

한끼얼마는 **레시피를 공유하고, 레시피의 가격을 제공하는 커뮤니티**입니다.

> **한끼얼마를 통해 레시피를 공유하고, 가성비 있는 한끼 챙기세요 🥘**

> [🚀 배포 URL](http://13.124.132.111/)

## 2. 👥 팀 소개

|배승원|서종훈|이지윤|정지환|김지훈|
|:---:|:---:|:---:|:---:|:---:|
|![img](https://github.com/seungwonbased/ssg-recipe-project/blob/main/assets/%EC%8A%B9%EC%9B%90.png)|![img](https://github.com/seungwonbased/ssg-recipe-project/blob/main/assets/%EC%A2%85%ED%9B%88.png)|![img](https://github.com/seungwonbased/ssg-recipe-project/blob/main/assets/%EC%A7%80%EC%9C%A4.png)|![img](https://github.com/seungwonbased/ssg-recipe-project/blob/main/assets/%EC%A7%80%ED%99%98.png)|![img](https://github.com/seungwonbased/ssg-recipe-project/blob/main/assets/%EC%A7%80%ED%9B%88.png)|
|![Static Badge](https://img.shields.io/badge/Team%20Leader-%23FE642E) ![Static Badge](https://img.shields.io/badge/Development-%235882FA)|![Static Badge](https://img.shields.io/badge/Development-%235882FA)|![Static Badge](https://img.shields.io/badge/UI%20%2F%20UX-%23BE81F7)|![Static Badge](https://img.shields.io/badge/%EA%B8%B0%ED%9A%8D%20%EB%B0%8F%20%EA%B4%80%EB%A6%AC-%23088A29)|![Static Badge](https://img.shields.io/badge/%EA%B8%B0%ED%9A%8D%20%EB%B0%8F%20%EA%B4%80%EB%A6%AC-%23088A29)|

## 3. 🗓️ 개발 기간 (23년 9월 1일 ~ 23년 9월 7일)

### 📌 일별 프로젝트 마일스톤

|일별|내용|
|:---:|---|
|1~7일차<br>(9/1 ~ 9/7)|- Flask 스터디|
|1일차<br>(9/1)|- 주제 선정, 기술 스택 및 협업툴 결정 (Notion, Discord)|
|3일차<br>(9/3)|- 세부 컨셉 기획, 세부 요구사항 정의|
|2~5일차<br>(9/2/ ~ 9/5)|- 필수 기능 개발|
|5일차<br>(9/5)|- 배포<br>- 개발 / 운영 환경 분리|
|5~7일차 <br>(9/5 ~ 9/7)|- 디버깅<br>- 추가 기능 구현|
|7일차<br>(9/7)|- 보고서 작성|

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
- ![Static Badge](https://img.shields.io/badge/AWS-FF9900?logo=Amazon%20AWS&logoColor=%23FFFFFF) Lightsail Instance
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
- \# 라운지: 자유롭게 토론
- \# 공지: 미팅, 일정, 회의록 공지
- \# 아이디어: 번뜩이는 아이디어
- \# 레퍼런스: 참고할만한 서비스, 자료 레퍼런스
- \# 이슈: 개발 및 프로젝트 진행에 있어 생기는 이슈
- \# 질문: 진짜 아무 질문이나
- \# 파일-및-코드: 파일 및 코드 공유
- \# 미팅: 보이스 & 페이스 미팅

## 5. ⚒️ 서비스 기능
### 5.1. URL 구조

```
/ : 메인 페이지, index.html
├──── /post : 게시글 Blueprint
│        ├──── /list : 게시글 리스트
│        ├──── /detail/<int:post_id> : 게시글 상세
│        ├──── /create : 게시글 작성 (HTTP Method: GET, POST)
│        ├──── /modify/<int:post_id> : 게시글 수정 (HTTP Method: GET, POST)
│        ├──── /delete/<int:post_id> : 게시글 삭제
│        └──── /like/<int:post_id> : 게시글 좋아요
├──── /comment : 댓글 Blueprint
│        ├──── /create/<int:post_id> : 댓글 생성 (HTTP Method: POST)
│        ├──── /modify/<int:comment_id> : 댓글 수정 (HTTP Method: GET, POST)
│        ├──── /delete/<int:comment_id> : 댓글 삭제
│        └──── /like/<int:post_id>/ : 댓글 좋아요
└──── /auth : 인증 Blueprint
         ├──── /signup : 회원 가입 (HTTP Method: GET, POST)
         ├──── /login : 로그인 (HTTP Method: GET, POST)
         └──── /logout : 로그아웃
```
### 5.2. 서비스 기능
#### 회원 가입
- 사용자가 회원 정보(이름, 이메일, 비밀번호)를 입력하여 새로운 계정을 생성
- 입력된 비밀번호는 해시로 암호화되어 데이터베이스에 저장됨
#### 로그인
- 등록된 사용자가 자신의 계정으로 로그인할 수 있음
- 인증을 위해 사용자 이름과 비밀번호를 확인하고 세션을 유지
#### 레시피 작성
- 로그인한 사용자가 레시피를 게시글 형태로 공유할 수 있음
- 요리 이름, 레시피 등의 텍스트 필드를 입력하고 데이터베이스에 저장됨
- 하단의 셀렉트 박스 형식으로 재료를 선택할 수 있고, 중량 또는 수량을 입력하면 가격이 계산됨
- 만약 로그인 상태가 아니라면 로그인 창으로 리다이렉트
#### 레시피 조회
- 작성한 레시피는 로그인한 사용자, 로그인하지 않은 사용자 모두가 볼 수 있음
- 계산된 가격이 레시피 하단에 출력됨
#### 레시피 수정
- 레시피 공유자 또는 관리자 권한을 가진 사용자만 해당 레시피 수정할 수 있음
- 선택된 레시피의 필드들(요리 이름, 레시피, 사진, 식품 카테고리, 가격)을 수정하고 데이터베이스에 업데이트
#### 레시피 삭제
- 레시피 공유자 또는 관리자 권한을 가진 사용자만 해당 레시피를 삭제할 수 있음
- 선택된 레시피는 데이터베이스에서 삭제됨
#### 레시피 좋아요
- 로그인한 사용자는 레시피에 좋아요를 누를 수 있음
- 자신의 레시피를 좋아요할 경우 불가능하다는 메세지가 출력됨
#### 레시피 리스트 조회
- 작성된 레시피가 10개 단위로 페이지로 나뉘어 렌더링됨
- 한 페이지에 보여지는 레시피 개수를 설정할 수 있고, 이전 / 다음 페이지 링크 또는 페이지 번호를 통해 페이지를 탐색할 수 있음
#### 검색
- 검색 창에서 전달 받은 데이터가 요리 이름, 레시피 내용, 레시피 공유자, 댓글 내용, 댓글 작성자 항목에서 OR 조건으로 검색한 질문을 반환
- 반환된 데이터는 리스트 조회와 같이 10개 단위로 나뉘어 렌더링됨
- 한 페이지에 보여지는 레시피 개수를 설정할 수 있고, 이전 / 다음 페이지 링크 또는 페이지 번호를 통해 페이지를 탐색할 수 있음
#### 댓글 작성
- 로그인한 사용자는 레시피에 댓글을 달 수 있음
- 로그인하지 않았다면 댓글 창이 비활성화되어 댓글을 달 수 없음
- 댓글의 텍스트 필드가 데이터베이스에 저장됨
#### 댓글 조회
- 댓글은 레시피 하단에서 리스트로 조회할 수 있음
#### 댓글 수정
- 댓글 작성자 또는 관리자 권한을 가진 사용자만 해당 댓글을 수정할 수 있음
#### 댓글 삭제
- 댓글 작성자 또는 관리자 권한을 가진 사용자만 해당 댓글을 삭제할 수 있음
#### 댓글 좋아요
- 로그인한 사용자는 댓글에 좋아요를 누를 수 있음
- 자신의 댓글을 좋아요할 경우 불가능하다는 메세지가 출력됨

## 6. 📚 서비스 특징 및 사용 라이브러리

### 6.1. 디렉터리 구조

```
📁 recipe-book
├──── 📁 app
│      ├──── 📁 api
│      ├──── 📁 static
│      ├──── 📁 templates
│      ├──── 📁 views
│      ├──── 📄 __init__.py
│      ├──── 📄 forms.py
│      └──── 📄 models.py
├──── 📁 config
│      ├──── 📄 __init__.py
│      ├──── 📄 default.py
│      ├──── 📄 develoment.py
│      └──── 📄 production.py
├──── 📁 logs
├──── 📄 .gitignore
├──── 📄 app.db
├──── 📄 requirements.txt
└──── 📄 README.md
```
#### 📁 app
> 💡: Flask 애플리케이션에 관련된 디렉터리 
- 📁 api: 공공데이터 API를 호출하는 클라이언트
- 📁 static: 이미지, css, js 등의 정적 파일을 저장하는 디렉터리
- 📁 templates: HTML 템플릿을 저장하는 디렉터리
- 📁 views: Blueprint 파일을 저장하는 디렉터리
- 📄 \_\_init\_\_.py: 애플리케이션 팩토리 함수가 있는 파일
- 📄 forms.py: 랜더링에 필요한 HTML 코드를 생성하며 웹 애플리케이션의 입력 폼을 정의하고 필드를 추가하는 Form 클래스가 정의되어 있는 파일
- 📄 models.py: 데이터를 객체에 담아 ORM을 이용하기 위한 클래스가 정의되어 있는 파일
#### 📁 config
> 💡: 환경 파일을 저장하는 디렉터리
- 📄 \_\_init\_\_.py: 패키지로 인식하기 위해 생성한 파일
- 📄 default.py: 모든 환경에서 공통으로 사용할 환경 변수를 저장하는 파일
- 📄 develoment.py: 개발 환경에서 사용할 환경 변수를 저장하는 파일
- 📄 production.py: 운영 환경에서 사용할 환경 변수를 저장하는 파일
#### 📁 logs
> 💡: 로그 파일을 저장하는 디렉터리, 운영 환경에서만 사용
#### 📄 requirements.txt
> 💡: 가상 환경에서 설치한 라이브러리들을 파일로 내보내 다른 환경에서도 쉽게 같은 환경을 구축할 수 있게 함

### 6.2. Database Schema
![img](https://github.com/seungwonbased/ssg-recipe-project/blob/main/assets/ERD.JPG)
- 참고: Image 테이블은 생성은 해놨지만, 아직 참조 관계를 구성하지 않음
	- 운영 서버에 적용되면 Post.id를 참조할 것임

### 6.3. Application Factory Pattern

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
- Flask 애플리케이션을 생성하고 초기화하는 디자인 패턴
	- 애플리케이션 객체를 Factory Function을 사용해 동적으로 생성하고 설정
		- 여러 개의 서로 다른 애플리케이션 인스턴스를 만들고 다른 환경(개발, 테스트 프로덕션)에서 실행할 수 있음
		- 이를 통해 본 프로젝트에서 개발과 운영 환경의 설정을 다르게 함
	- 장점
		- 확장성 향상
		- 설정과 환경 관리의 용이

### 6.4. Blueprint
- Flask 블루프린트는 웹 애플리케이션을 여러 개의 독립적인 모듈로 나누고, 각 모듈을 개별적으로 작업하거나 재사용할 수 있게 해줌
	- 라우팅 함수의 집합
- 웹 애플리케이션을 개발할 때 코드를 더 구조화하고 관리하기 쉽게 만듬
- 장점
	1. 모듈화
		- 각 기능을 독립적인 블루프린트로 정의하여 모듈화된 코드 작성이 가능하므로 유지 보수와 확장이 용이
	2. . 라우팅 분리
		- URL 라우팅을 각 블루프린트 내에서 관리하므로 충돌을 방지하고 URL 구조를 구성하기 쉬움
	3. 코드 재사용
		- 비슷한 기능을 다른 애플리케이션에서 재사용할 수 있음
- 본 프로젝트에서는 애플리케이션을 목적에 따라 모듈로 분할해 라우팅 함수를 작성했음

### 6.5. Server-Side Rendering
- Front-end 애플리케이션 개발이 불가능해 웹 애플리케이션의 뷰를 서버에서 생성해 클라이언트에게 전달하는 방식인 SSR 사용

### 6.6. Object-Relational Mapping
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
# Python code
sub_query = db.session.query(Comment.post_id, Comment.content, User.username)   .join(User, Comment.user_id == User.id).subquery()
```
```sql
-- SQL query
SELECT * 
FROM post_list INNER JOIN "User" ON post_list.user_id = "User".id 
LEFT OUTER JOIN sub_query ON sub_query.post_id = post_list.id 
WHERE post_list.subject ILIKE 'search_value';
```

### 6.7. Flask ORM Library: SQLAlchemy
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

### 6.8. Models
- Models.py 파일에 ORM을 사용해 모델을 정의함
	- 데이터베이스 테이블과 상호작용하기 위한 클래스를 정의
- 클래스의 각 속성은 매핑되는 테이블의 Column과 일치
- 데이터 유형과 제약 조건 또한 지정

### 6.9. @Decorator
#### @bp.route
- 애플리케이션에서 블루프린트 객체를 사용해 URL 경로에 따라 어떤 함수가 실행될 지를 정의하는 데 사용되는 데코레이터
- @app.route 또한 URL 경로와 함수 간의 매핑을 정의하지만, @app.route는 Flask 애플리케이션 객체('app')에 직접 라우팅 함수를 연결하는 데 사용되는 반면, @bp.route 데코레이터는 블루프린트 객체에 라우팅 함수를 연결하는 데 사용됨
	- 블루프린트는 Flask 애플리케이션을 모듈화하고 라우팅을 구조화하는 데 사용됨
	- 블루프린트를 사용한 라우팅 함수들을 관리하는 데 유용하며 모듈화, 확장 가능의 장점이 있음

### 6.10. 'request' 객체
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

### 6.11. Flask Form
- Flask 애플리케이션에서 웹 폼을 쉽게 처리하기 위한 확장 라이브러리
- 웹 폼을 쉽게 생성하고, Form validation, 데이터 수집, 에러 처리 등을 할 수 있음
- CSRF(Cross-Site Request Forgery) 방지 같은 보안 기능도 내장되어 있음
	- CSRF 토큰 코드를 삽입해야 정상적으로 데이터 전송 가능
- 사용 방법
	1. FlaskForm을 상속 받는 Form 클래스를 정의
	2. View의 라우팅 함수에서 Form 인스턴스를 생성하고 사용
		- POST 요청일 때 검증 작업 등
	3. HTML 템플릿 파일에서 웹 폼을 렌더링하고 사용자에게 입력을 받음

### 6.12. 페이징 - Pagenation
- SQLAlchemy 라이브러리의 Pagination 객체 사용
- 레시피 리스트가 담긴 객체에 pagenate 함수 적용
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

### 6.13. 회원가입 - WTForms
- 웹에서 폼을 정의하고 검증하기 위한 라이브러리
	- 웹 폼을 쉽게 생성하고, 사용자로부터 데이터를 수집하고 검증할 수 있음
- 회원가입을 위해 FlaskForm을 상속 받아 UserCreateForm 생성
- PasswordField, EmailField을 import
	- PasswordField: 사용자의 비밀번호를 입력받을 때 이 필드를 사용하면 비밀번호 입력을 안전하게 처리하고 Validation도 할 수 있음
		- 라우팅 함수에서 generate_password_hash 함수로 암호화
	- EmailField: StringField와 동일하지만 템플릿 자동 변환으로 사용시 \<input type="email">로 변환됨

### 6.14. 로그인 - session, g
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

## 7. 🚀 배포
### AWS Lightsail
- AWS Lightsail 서비스를 사용해 배포
- 저렴하고, 아주 간단하게 배포가 가능해 선택하였음

### 인스턴스 스펙
- RAM: 1GB
- vCPU: 2
- SSD: 40GB
- OS: Ubuntu 20.04

### 원격 관리 방법 - SSH
- Private key 발급 후 다음과 같은 명령어로 서버에 접속
```bash
ssh -i ~/PrivateKeys/ssgrecipe.pem ubuntu@static_ip
```

### 초기 서버 환경 설정
```bash
git clone https://github.com/seungwonbased/ssg-recipe-project.git
```
- git 명령어로 clone 해온 뒤에 requirements.txt를 통해 라이브러리 설치
	-> 개발 환경과 같은 환경으로 서버 구성
- 서버 환경 변수 설정
- 데이터베이스 초기화 및 migrate, upgrade

### config 디렉터리 생성
- 개발 / 운영 환경을 나누기 위해 config 파일 또한 다음과 같이 분리
```
📁 config
├──── 📄 __init__.py
├──── 📄 default.py
├──── 📄 develoment.py
└──── 📄 production.py
```

### 웹 서버의 동적 페이지 요청 처리
#### WSGI (Web Server Gateway Interface, Whiskey)
- Python 웹 애플리케이션과 웹 서버 간의 표준화된 인터페이스
- WSGI는 웹 서버와 웹 애플리케이션 프레임워크 또는 애플리케이션을 분리해 개발자가 서로 다른 서버 및 애플리케이션을 조합하여 사용할 수 있도록 중간 계층 역할을 함
- 즉, Python으로 작성된 여러 웹 애플리케이션 프레임워크와 웹 서버를 통합하는 데 사용됨
- Flask는 WSGI 애플리케이션이고, WSGI 서버에서 요청을 받아 동작
##### Gunicorn
- 운영을 위해 운영 서버에 WSGI인 Gunicorn 설치
- Gunicorn을 리눅스에서 서비스로 등록하기 위해 환경 변수 파일 생성 및 서비스 파일 생성
- 서비스 자동 실행 설정
```bash
sudo systemctl enable ssgrecipe.service
```

#### Web Server
- 웹 서버는 클라이언트로부터 HTTP 요청을 수신하고, 정적 파일(HTML, CSS, 이미지 등)을 서비스하며, 동적 컨텐츠를 생성하는 웹 애플리케이션 서버나 애플리케이션 서버에 요청을 전달하는 역할
- 주로 정적 컨텐츠를 서비스하는 역할을 하며, 웹 서버로는 Apache, Nginx, IIS 등이 있음
- 로드 밸런싱: 여러 웹 서버 인스턴스 간에 트래픽을 분산
- 보안 및 인증: SSL/TLS 인증서 관리 및 보안 설정을 처리
- 리버스 프록시: 동적 컨텐츠를 생성하는 애플리케이션 서버로 요청을 전달
##### Nginx
- 운영 서버의 웹 서버로 Nginx를 설치
- 비동기 기반 구조라 더 적은 리소스를 사용해서 요청을 처리할 수 있음
- Nginx의 설정을 변경
	- 80 포트로 서비스하도록 함
	- static 경로를 지정해 정적 리소스를 서빙할 수 있도록 함

### Logging
- 운영 환경에서는 보안 이슈로 FLASK_DEBUG가 False로 되어있으므로 로그를 파일로 출력하도록 함
- 출력되는 로그 레벨은 2단계 INFO, 일반적인 정보를 출력

### Database Migration
- 운영 서버에서는 SQLite가 아닌 오픈소스 RDBMS인 PostgreSQL를 사용하기로 결정
	- 여러 가지 이유가 있는데, 대표적인 이유는
		- SQLite는 서버를 따로 두고 통신할 수 없기 때문에 인스턴스가 있는 로컬에서 DB를 운용해야 함
		- 아직은 데이터를 대규모로 처리할 일은 없지만 운영 서버에 배포한 만큼 그 부분을 고려하고 싶었음, SQLite는 동시성에 제한이 있어 운영 서버에는 부적합
- AWS에서 PostgreSQL RDS 데이터베이스를 생성
- ***ORM의 마법***으로 config 파일에서 DB 엔드포인트, user, pw, url 수정만으로 설정 완료
	- 스키마나 쿼리, 애플리케이션 코드를 단 한 개도 변경하지 않음
	- 감동의 눈물을 흘림
- 서버에서 다음 명령어를 입력하면 마이그레이션 완료!
```bash
flask db init
flask db migrate
flask db upgrade
sudo systemctl restart ssgrecipe.service
```

## 8. 🔧 Issue & Troubleshooting
> ✅: 해결 이슈
> ❓: 미해결 이슈

### 8.1. Open API 데이터 호출 실패
- 식품 가격 정보를 받아오는 Open API에서 원래는 정상적으로 데이터 호출이 되었음
- 어느 순간부터 데이터 호출이 실패하더니, 아예 동작하지 않기 시작
- 원인은 Flask 애플리케이션 실행시 호출되는 API 호출 클라이언트에 이상한 루프를 짜놔서 일일 호출 한도 초과가 된 것
> ✅ 해결: API 호출 클라이언트를 수정하고, 사실은 API 호출은 한 번만 해도 되기 때문에 별도의 모듈로 작성하는 방향으로 변경

### 8.2. Select Box에서 데이터 받아오기 실패
- 사용자에게 레시피를 입력받을 때, 하단에서 Select box로 재료를 입력 받음
- 하지만 선택된 값이 계속 None으로 넘어옴, 반면 수량을 입력하는 Text input은 정상적으로 넘어옴
> ✅ 해결: Form을 정의할 때 수량에 해당하는 필드는 Text input이기 때문에 StringField 객체가 되어야 되는 것은 맞았지만, 재료는 Select box이기 때문에 Form에서 필드가 SelectField여야 됐음

### 8.3. Select Box 동적 생성
- 레시피마다 들어가는 재료의 수가 다양하기 때문에 Select box의 수가 동적으로 추가됐으면 함
> ✅ 해결: 템플릿 엔진 하단에 JS 코드를 작성함, 추가 버튼 클릭 시 createElement 함수를 호출해 \<div> 태그 생성

### 8.4. 동적으로 생성한 Select Box에서 데이터 받아오기 실패
- 8.2.에서 해결한 동적 생성한 Select Box에서 데이터를 받아오는데 실패
- 뭔가 동적으로 배열로 받고 싶은데, 도무지 방법을 모르겠음
> ❓ 미해결: 결국 현재까진 Select box 개수를 정적으로 설정하고 한정된 수의 재료만 입력받을 수 있음, 템플릿 엔진 문법이든, HTML 코드든 더 딥다이브 해볼 것

### 8.5. 이미지 불러오기, 엑스박스와의 씨름
- 레시피에 이미지를 업로드하면 구성해둔 디렉터리에 정상적으로 삽입은 되지만 레시피를 조회할 때는 HTML에서 해당 경로의 이미지를 불러올 수 없음, 페이지 소스를 보면 경로는 분명 맞는데 엑스박스가 뜸
- DB에 정상적으로 삽입은 되지만 불러올 수 없음
> ✅ 해결: 이미지 저장 경로를 임의로 주면 안 되고, static 디렉터리 안에 생성해야 이미지를 정상적으로 서빙할 수 있음

### 8.6. 클라이언트 전용 DB, SQLite
- 처음 개발을 시작할 때는 운영 서버로 배포까지는 할 생각이 없어서 로컬에서 가볍게 쓸 수 있는 클라이언트 전용 DB인 SQLite를 사용
- AWS에 배포하게 되면서 7.에 작성한 이유로 DB 서버를 분리하고 싶어짐
> ✅ 해결: AWS RDS에 PostgreSQL로 DB 서버를 생성, ORM을 채택한 덕에 아주 쉬운 마이그레이션 작업이 되었음

### 8.7. 도메인이 없어서 SSL 적용 불가능
- SSL 인증서를 발급 받아서 보안을 강화하고 HTTPS 접속이 되었으면 함
> ❓ 미해결: 도메인 네임을 발급받지 않으면 Let's Encrypt에서 SSL 인증서 발급 불가능

### 8.8. 똑같은 코드를 배포했는데, 작동이 안되네
- requirements.txt를 통해 개발 환경과 똑같은 라이브러리를 설치하고, 웹 서버와 WSGI도 정상적으로 돌아가고 있는데 작동이 되지 않음
> ✅ 해결: 운영 환경에서 FLASK_DEBUG를 True로 바꾸기 싫어 로그를 txt로 저장하도록 함, 이를 통해 APP_CONFIG_FILE 인식이 안돼 오류가 나고 있었음, 운영 서버의 alias 설정을 통해 해결

### 8.9. 재료 DB를 수집하는 방안에 대한 의견 차이
- 이상적 목표 : 신세계 리테일 브랜드 내 가격 API 도입
- 목표의 근거
	1. 신세계 내 커뮤니티 커머스 발전 가능 
	2. 실시간으로 가격 DB 업데이트 가능
- 현실적 문제 : 신세계 API가 신세계 플랫폼에 입점한 상품 판매자에게만 허용되어서 사용 불가능
- 대안
	- 공공데이터 API
		-  장점 : 기술적으로 API 도입 기능 구현 가능
		- 단점 : '레시피'라는 기획 의도를 충족시키기에는 데이터로 제공되는 품목이 제한됨
	- 이마트몰(신세계 리테일 브랜드)에서 직접 가격 조사
		-  장점 : 기획 취지에 맞게 '레시피'에 자주 등장하는 재료 선정 가능 
		- 단점 : 데이터의 실시간성, 신뢰성 이슈
> ✅ 해결: 공공 API를 도입하고, 임의로 조사한 가격 데이터를 혼합하여 DB 구성 각 대안의 장단점을 상호 보완

## 9. ☕️ 회고 

### 김지훈
- 이번 프로젝트에서 디렉토리를 이해하는 것에 주안점을 뒀습니다. 팀원 전체가 Flask 학습을 하는 과정에서 다른 조원에 비해 이해속도가 현저히 느렸습니다. 기본적인 디렉토리 구성을 이해하지 못한 것이 원인이었습니다. 이를 해결하기 위해 이번 프로젝트의 디렉토리 구성과 그 뜻을 모니터 한 켠에 띄워놓고 반복적으로 학습했습니다. 
- 개발 과정에 뚜렷이 기여할 수 없는 상황이었기에, 백데이터 수집 등 프로젝트 기획 부분에 주도적으로 임했습니다. 특히 이 과정에서 ‘Lean Startup’ 과 ‘Agile’ 방식에 대해 각각의 특징과 둘 간의 차이점을 명확히 이해할 수 있었습니다. 이를 포함하여 제가 학습한 부분을 노션 문서로 작성하여 팀원들에게 공유하였습니다.  
- 이번 프로젝트의 가장 큰 성과는 ‘이해할 수 있는 READ.ME’를 얻었다는 것입니다. 기초가 부족하여 깃헙에 있는 다른 프로젝트의 리포트들을 해석하기 어려웠는데, 팀장인 승원님이 작성해주신 최종 리포트는 개발 과정을 알고 있기에 빠르게 이해할 수 있었습니다. 향후 이를 토대로 다른 게시판을 직접 만들어보며 학습할 예정입니다. 팀 내 커뮤니케이션이 원활하여, 테크니컬 지식이 부족한데도 프로젝트에 기여할 수 있었습니다. 조원들에게 감사를 표합니다.

### 서종훈
- Flask를 사용해서 웹 개발해본 적이 없었는데, 이번 프로젝트를 경험함으로써 좋은 경험이 되었고 ORM 기능을 적용하면 DB 마이그레이션도 간편하고 DB를 객체화 후에 사용하면서 따로 SQL문을 작성하지 않아도 되는 것에 편리함을 느껴 이번 프로젝트에 사용 경험을 토대로 추후 개발에도 ORM에 대한 개념을 복습 후에 적용하려 합니다. 개발 과정에서 경로 설정 문제나 DB 연동 문제, 이미지 파일 송/수신등 에러도 많이 발생하였는데 최대한 관련 문서 검색을 통해 해결하거나 팀원분들과 강사님의 도움을 받아 해결 했습니다. 가장 문제를 겪었던 파트인 레시피 게시물에서 이미지를 업로드하는 부분이었는데, 이미지 전송이 완료되면 저장 하려는 이미지 파일의 이름명을 DB에 넣고 가공 처리과정의 파트를 거쳐야 하는데 가공 처리과정의 로직을 이해하기 쉽게 설명해주셔서 많은 공부가 되었습니다. 개발 과정중 모르거나 헷갈리는 부분은 추후에 셀프 코드 리뷰를 통해 학습 후 정리할 예정입니다.

### 이지윤
- html과 css에 대해서 여러가지 기능을 실습하면서 프론트에 대한 이해도가 높아졌습니다. 기초코드 작성은 하였지만 추가 기능 구현에 대한 이해도가 부족하기 때문에 추후에는 더 공부하여 백엔드 기능 구현에도 도전해보고 싶습니다.

### 배승원
- 주로 Spring 프레임워크로 애플리케이션을 개발하다가 Flask를 처음 사용해봤습니다. 개발을 진행하며 프레임워크가 간결하고 가벼워 본 프로젝트에 최적이라는 생각을 했습니다. JPA를 사용했던 경험을 토대로 본 프로젝트에도 ORM을 적용해보았는데, 역시나 제 스타일입니다. 개발 중에는 물론이고, 특히 초반 개발 환경에서 쓰던 Sqlite를 운영 서버에 배포할 때 PostgreSQL로 마이그레이션 했는데, 감동의 눈물을 흘렸습니다. 짧은 기간이었지만 팀원들과 커뮤니케이션이 아주 만족스럽고, 덕분에 테크니컬한 부분에 집중할 수 있었습니다. 즐거웠습니다.

### 정지환
- Flask 프레임워크를 활용한 프로젝트를 통해 저는 다양한 것들을 배우고 성장할 수 있었습니다. 책, 강의 자료, 그리고 팀원들과의 스터디를 통해 Python, Flask, 그리고 HTML의 기본 개념과 구조를 습득하고 실제로 코드를 작성하며 응용하는 과정은 매우 유익했습니다. 특히, 쿼리문을 사용하는 대신 ORM을 사용해보면서 SQL 문법을 배우지 않아도 직관적으로 데이터베이스와 상호작용할 수 있는 장점을 경험했습니다. ORM의 활용으로 인해 복잡한 SQL 문법에 대한 어려움 없이 보다 간편하게 데이터 조작 및 관리가 가능해졌습니다. 그러나 파이썬과 DB 구조에 대한 전반적인 이해 부족으로 인하여 HTML 사진 저장 기능은 구현할 수 있었으나 데이터베이스에 저장하는 과정에서 어려움을 겪었습니다. 창의적인 아이디어로 팀원들에게 인정을 받았지만 기능을 구현하지 못하는 한계가 저에게 동기부여가 되었습니다. 지속적인 리뷰와 자기계발 노력으로 능력을 향상시키며 다양한 프로젝트에 도전하여 상상 속에서만 그렸던 것들을 현실로 만들어내는 개발자가 되겠습니다.