from django.shortcuts import get_object_or_404, render
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋 -> 모델의 Blog 객체 목록을 변수에 저장
    return render(request, 'home.html', {'blogs': blogs})

def hello(request):
    return render(request, 'hello.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk= blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})