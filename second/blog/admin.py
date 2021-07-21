from django.contrib import admin
from .models import Blog

admin.site.register(Blog) # /admin에 Blog 모델 연동하기