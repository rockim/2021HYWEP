from rest_framework import viewsets
from .serializers import WebtoonSerializer
from .models import Webtoon, Titleid
from django.shortcuts import render
from urllib import parse
from .forms import WebtoonForm
from comment_parse import parse_comment
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = WebtoonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WebtoonForm()
    return render(request, 'register.html',{'form':form})

def webtoon_list(request):

    webtoonList = Webtoon.objects.all()
    return render(request, 'webtoon_list.html',{'webtoonList':webtoonList})

def specific(request):
    url = request.build_absolute_uri().split("/")[-1] # wsgirequset를 uri string으로 바꾸는 함수
    title = parse.unquote(url) # url 한글 유니코드 변환
    titleidList = Titleid.objects.get(title__iexact=title)# title이 있는 titleid 오브젝트에서 titleid 와 day object 가져오기
    parse_comment(titleidList.title_id,titleidList.day)
    return render(request, 'specific.html',{'titleidList':titleidList})

#def comment(request):

class WebtoonViewSet(viewsets.ModelViewSet):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonSerializer
