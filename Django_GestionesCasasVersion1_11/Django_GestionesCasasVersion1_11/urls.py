"""Django_GestionesCasasVersion1_11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from . import settings
from . import views


urlpatterns = [
    url(r'^login/$', views.login_page, name='login'),
    url(r'^login/savechat/$', views.save_chat, name='xat'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', views.search, name='search'),
    url(r'^calendar/', include('calendarium.urls')),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
     #   'document_root': settings.MEDIA_ROOT
	
    #}), 
]