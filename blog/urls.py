from django.urls import path

from blog.views import AddComment, AddPost, Detail, EditComment, DeleteComment

urlpatterns = [
    path('post/<int:pk>', Detail.as_view(), name='detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post/<int:pk>/add_comment/', AddComment.as_view(), name='add_comment'),
    path('post/edit/<int:pk>', EditComment.as_view(), name="edit_comment"),
    path('post/delete/<int:pk>', DeleteComment.as_view(), name="delete_comment")
]