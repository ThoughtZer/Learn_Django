# -*- coding: utf-8 -*-
import xadmin
from models import *


class UserAdmin(object):
    list_display = ['id', 'u_name']
    # 希望展示出的内容就直接在list_display写出model的字段名
    pass


xadmin.site.register(User, UserAdmin)


# 注册的时候是前面是views中的model名，后面是这里的class名

class ArticleAdmin(object):
    list_display = ['id', 'title', 'desprition']
    pass


xadmin.site.register(Article, ArticleAdmin)
# 注册的时候是前面是views中的model名，后面是这里的class名
