"""github_issues URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from issues import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^geturl', views.getUrl, name='geturl'),
    url(r'^admin/', admin.site.urls),
    url(r'^issues/', include('issues.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^login/$', RedirectView.as_view(url='/login/github')),


]
