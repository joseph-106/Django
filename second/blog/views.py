from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋 -> 모델의 Blog 객체 목록을 변수에 저장
    return render(request, 'home.html', {'blogs': blogs})