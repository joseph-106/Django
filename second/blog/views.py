from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects
    #블로그 모드 글들을 대상으로
    blog_list = Blog.objects.all().order_by('-pub_date')
    #블로그 객체 3개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts':posts})

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

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST 방식
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid(): # 모든 입력 공간이 제대로 입력됐다면
            post = form.save(commit=False) # 아직 저장하지 않은 상태로 모델 객체 반환
            post.pub_date = timezone.now() # 따로 자동으로 처리
            post.save() # 저장
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 -> GET 방식
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})