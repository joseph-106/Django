from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋 -> 모델의 Blog 객체 목록을 변수에 저장
    return render(request, 'home.html', {'blogs': blogs})

def hello(request):
    return render(request, 'hello.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk= blog_id) #이용자가 원한 몇 번 블로그 객체

    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request): #new.html의 form에서 입력받은 내용을 DB로 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #객체에 해당하는 내용들을 /admin 에 저장
    return redirect('/blog/'+str(blog.id)) #글 작성을 완료하면 해당 글 detail이 뜨도록