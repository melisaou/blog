from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CommentForm, PostForm
from blog.models import Post, Comment

class Home(ListView):
    model = Post
    template_name = 'index.html'

class Detail(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm

class AddComment(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class EditComment(UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    fields = ['comment']

class DeleteComment(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')
