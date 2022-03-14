from statistics import mode
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post

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