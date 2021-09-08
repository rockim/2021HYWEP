from rest_framework import serializers
from .models import Webtoon, Titleid

class WebtoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webtoon #모델 설정
        fields = ('id','title','author','rate')#필드설정

class TitleidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titleid
        fields = '__all__'