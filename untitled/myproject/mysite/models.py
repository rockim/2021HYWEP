from django.db import models

# Create your models here.
class Webtoon(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rate = models.FloatField()

    def __str__(self):
        return self.title

class Titleid(models.Model):
    title = models.CharField(null=True,max_length=100)
    day = models.CharField(null=True,max_length=30)
    title_id = models.IntegerField()

    def __str__(self):
        return self.title

class SpecificWebtoon(models.Model):
    no = models.IntegerField()
    star_point = models.FloatField()
    date = models.CharField(null=True,max_length=30)

    def __int__(self):
        return self.no

class BestComment(models.Model):
    best_comment = models.CharField(max_length= 5000)

    def __str__(self):
        return self.best_comment