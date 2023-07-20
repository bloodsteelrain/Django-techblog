# Django Blog

- Django를 이용해 자신만의 Blog를 제작하는 프로젝트입니다.

## 1. 목표와 기능

### 1.1 목표

- Django를 이용해 CRUD 기능을 갖춘 Blog를 만드는 것.

### 1.2 기능

0. 메인페이지
1. 블로그 CRUD 기능
   1. 게시글 작성
   2. 게시글 목록
   3. 게시글 상세보기
   4. 게시글 수정
   5. 게시글 삭제
   6. 게시글 카테고리별 목록
   7. 게시글 검색
2. 로그인/회원가입 기능
   1. 회원가입
   2. 로그인
   3. 게시글 CRUD에 인증 기능 추가
3. 기타 추가 기능
   1. 게시글 조건 검색
   2. 게시글 조회수
   3. 게시글 작성 시 이미지 업로드
   4. 댓글 CRD
   5. 대댓글 CRD

## 2. 개발 환경 및 배포 URL

### 2.1 기술 스택

- <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
- <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
- <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=SQLite&logoColor=white">

### 2.2 개발 환경

- Django==4.2.3
- Pillow==10.0.0

### 2.3 배포 URL

- 미정

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조

```
📦 Django-Techblog
├─ app
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ views.py
│  └─ wsgi.py
├─ blog
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_initial.py
│  │  ├─ 0003_hashtag_comment.py
│  │  ├─ 0004_post_views.py
│  │  ├─ 0005_comment_parent_comment.py
│  │  ├─ 0006_post_image.py
│  │  ├─ 0007_alter_post_image.py
│  │  ├─ 0008_alter_post_image.py
|  |  ├─ 0009_remove_comment_parent_comment_reply
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ blog
│  │     ├─ form_error.html
│  │     ├─ post_detail.html
│  │     ├─ post_edit.html
│  │     ├─ post_form.html
│  │     └─ post_list.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ templates
│  ├─ base.html
│  └─ index.html
├─ user
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ user
│  │     ├─ user_login.html
│  │     └─ user_register.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ requirements.txt
├─ .gitignore
└─ README.md
```

### 3.2 데이터베이스 모델

![blog_diagram](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/f0fbc992-98b5-49d6-b13e-b99423ae5d88)

### 3.3 개발 일정

2023.07.17 ~ 2023.07.20

## 4. UI

- 메인 페이지
  ![127 0 0 1_8000_](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/0005c4cd-1336-49bc-93c2-dcefeb472831)

- 게시글 목록 페이지
  ![127 0 0 1_8000_blog_](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/6d14397b-535d-419a-b4e6-775ee056c3fc)

- 게시글 상세보기 페이지
  ![127 0 0 1_8000_blog_detail_19_](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/b45aca71-3a6a-4509-9a2b-102f5f3c61ab)

## 5. 기능

1. 게시글 작성
   ![글작성](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/d3d15e14-e333-45c6-9ea2-d79c0128e73a)

2. 게시글 수정
   ![글수정](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/96328895-e652-464d-a39f-ca614197823b)

3. 게시글 삭제
   ![글삭제](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/95f56632-0fd4-472f-9877-c7fa52ca0a2d)

4. 댓글 작성
   ![댓글작성](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/84951dc5-f872-46f0-a898-78a235a09ab9)

5. 카테고리 정렬
   ![카테고리](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/098a4a02-7024-4126-8bdf-4a3527e009a3)

6. 검색
   ![검색](https://github.com/bloodsteelrain/Django-techblog/assets/131739343/4edef2f0-f4c7-41bc-b0aa-69e54ca124a5)
