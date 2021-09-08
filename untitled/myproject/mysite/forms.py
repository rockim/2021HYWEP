from django.forms import ModelForm
from .models import Webtoon

class WebtoonForm(ModelForm):
    class Meta:
        model = Webtoon
        fields = ['id','title','author','rate']
