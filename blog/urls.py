from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 전체 목록 조회
    path('', views.Index.as_view(), name='list'),
    # 글 카테고리별 목록 조회
    path('list/<str:c_name>/', views.CategoryView.as_view(), name='category'),
    # 글 상세페이지 조회
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # 게시글 작성
    path('write/', views.Write.as_view(), name='write'),
    # 게시글 수정
    path('detail/<int:pk>/edit/', views.Update.as_view(), name='edit'),
    # 게시글 삭제
    path('detail/<int:pk>/delete/', views.Delete.as_view(), name='delete'),
    # 댓글 작성
    path('detail/<int:pk>/comment/write/',
         views.CommentWrite.as_view(), name='cm-write'),
    # 댓글 작성
    path('detail/<int:post_pk>/comment/<int:comment_pk>/reply/',
         views.CommentReply.as_view(), name='cm-reply'),
    # 댓글 삭제
    path('detail/comment/<int:pk>/delete/',
         views.CommentDelete.as_view(), name='cm-delete'),
    # 태그 작성
    path('detail/<int:pk>/hashtag/write/',
         views.HashTagWrite.as_view(), name='tag-write'),
    # 태그 삭제
    path('detail/hashtag/<int:pk>/delete/',
         views.HashTagDelete.as_view(), name='tag-delete'),
]
