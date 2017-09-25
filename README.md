### 关于python语言框架Django的学习

---

__startapp__

    django-admin startapp appname

__create Model__

    python manage.py migrate 	# 这条命令非常重要
    python manage.py makemigrations appname
    python manage.py migrate  appname

__xadmin__

    # create adminx.py
    # config urls.py

    from django.conf.urls import url
    from django.contrib import admin
    import xadmin

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^xadmin/', xadmin.site.urls)
    ]
