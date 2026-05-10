"""conduit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path
from django.views.generic import RedirectView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('articles:article-list', request=request, format=format),
        'user': request.build_absolute_uri('/api/user/'),
        'register': request.build_absolute_uri('/api/users/'),
        'login': request.build_absolute_uri('/api/users/login/'),
        'profile': request.build_absolute_uri('/api/profiles/<username>/'),
        'follow': request.build_absolute_uri('/api/profiles/<username>/follow/'),
    })


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^$', RedirectView.as_view(url='/api/', permanent=False)),
    re_path(r'^api/$', api_root, name='api-root'),

    re_path(r'^api/', include('conduit.apps.articles.urls', namespace='articles')),
    re_path(r'^api/', include('conduit.apps.authentication.urls', namespace='authentication')),
    re_path(r'^api/', include('conduit.apps.profiles.urls', namespace='profiles')),
]
