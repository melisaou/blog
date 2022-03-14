from django.urls import path

from blog.views import AddPost, Detail

urlpatterns = [
    path('post/<int:pk>', Detail.as_view(), name='detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]