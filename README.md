# 🖼og-assignment
오픈갤러리 Django 개발 테스트 과제입니다.

# 🎨Intro
* 등록된 작가와 작품의 정보를 조회
* 작가 계정은 작품과 전시 등록 가능
* 관리자 계정은 작가 등록 승인 처리와 작가 통계 조회 가능
* **기간:** 2022.09.07 ~ 2022.09.14

# 🖌Project
### 사용 기술
* Python 3.8
* Django 4.1.1
* JavaScript ES6
* DRF 3.13
* Django Template Engine

### 구현 기능
* 페이지네이션을 이용한 작가 및 작품 목록 조회
* 작가 등록 신청
* 작가 등록 신청 내역 조회 및 승인/반려 처리
* 작가 통계 조회 - 100호 이하 작품 개수, 작품 평균 가격, 전시 횟수
* 작품 및 전시 조회
* 작가/작품 조회 페이지 및 작가 등록 신청 내역 조회 페이지에서 검색 기능

### 로컬 서버 세팅
1. 레포지토리 클론
```
git clone https://github.com/zeonga1102/og-assignment.git
```
2. 패키지 설치
```python
pip install -r requirements.txt
```
3. 마이그레이션
```
python manage.py makemigrations
python manage.py migrate
```
4. 서버 실행
```
python manage.py runserver
```

### ERD
![og-assignment](https://user-images.githubusercontent.com/71905164/189887098-39f8b010-dbee-43bb-9047-713a0c20201c.png)
