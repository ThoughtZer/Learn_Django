# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import *
from django.http import HttpResponse, JsonResponse
import time
import os

from myDjango.settings import MEDIA_ROOT


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


def Upload_File(request):
    File = request.FILES.get('FileArgName', None)
    filePath = saveFile(File)
    file = FileUpload(file_name=File, file_path=filePath)
    file.save()
    return JsonResponse({'ret': 0, 'msg': 'success'})


# 自己定义的写入文件的方法，而且改变文件名加上时间戳
def saveFile(caseFile):
    FileName = caseFile.name
    timestamp = str(int(time.time()))
    pos = FileName.rfind('.')
    FileName = FileName[:pos] + '_' + timestamp + FileName[pos:]
    destination = open(os.path.join(MEDIA_ROOT, FileName), 'wb+')
    # UPLOAD_DIR也是一定路径常量，可以定义到settings中
    for chunk in caseFile.chunks():
        # 分块写入文件
        destination.write(chunk)
    destination.close()
    return FileName
