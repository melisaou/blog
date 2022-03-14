from pyexpat import model
from statistics import mode
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CommentForm

from blog.models import Post, Comment

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class Detail(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class AddComment(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    # fields = '__all__'
    form_class = CommentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.name_id = self.request.user.id
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class EditComment(UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    fields = ['body']

class DeleteComment(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')
