# EMR_API_Server
Electronic Medical Record API Server

#### Requirements
* python 3.6 이상
* PostgreSQL을 이용해 구축된 CDM 데이터베이스

#### 설치 방법

main_default.cfg를 main.cfg로 복사 후, 파일을 직접 수정합니다.

main.cfg의 내용은 다음과 같습니다.

* SQLALCHEMY_DATABASE_URI: 연결할 CDM DB의 SQLAlchemy URI
* SCHEMA_CDM: CDM 데이터가 속해있는 Schema 이름

#### 접속 방법

* 실행 후, url 접속
 http://localhost:5000
