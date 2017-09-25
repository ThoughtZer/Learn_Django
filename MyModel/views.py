from django.shortcuts import render
from models import *
from django.http import HttpResponse, JsonResponse


# Create your views here.

def UserList(request):
    allUser = User.objects.all()
    list = []
    for user in allUser:
        list.append(user)
    return render(request, 'user_list.html', {'users': list})


def ArticleList(request, UserId):
    user_id = UserId
    user = User.objects.get(id=UserId)
    allArticle = Article.objects.filter(article_author_id=user_id)
    list = []
    for article in allArticle:
        list.append(article)
    return render(request, 'article_list.html', {'articles': list, 'user': user})


def ArticleDetail(request, ArticleId):
    article_id = ArticleId
    article = Article.objects.get(id=article_id)
    return render(request, 'article.html', {'article': article})
