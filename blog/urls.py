from django.urls import path
from blog import views
from blog.views import (PostListView,
                        # PostDetailView,
                        PostCreateView,
                        PostUpdateView,
                        PostDeleteView,
                        UserPostListView,
                        )
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/', views.postDetail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:pk>/comment/',views.writeComment,name='write-comment'),
    # path('post/<int:pk>/comment/postcomment/',views.postComment,name='post-comment'),
    path('about/',views.about, name='blog-about'),

]