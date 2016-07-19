"""myProject URL Configuration

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
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin

from posts import views

urlpatterns = [
	url(r'^$', views.post_home, name='home'),
    url(r'^crear/', views.crear_post, name='post'),
    url(r'^contenido/', views.contenido_post, name='contenido'),
    url(r'^detalle/(?P<id>\d+)/$', views.detalle_post, name='detalle'),
    url(r'^editar/(?P<id>\d+)/$', views.actualizar_post, name='actualizar'),
    url(r'^borrar/(?P<id>\d+)/$', views.borrar_post, name='borrar'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG==True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
