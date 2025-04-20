from django.contrib import admin
from django.urls import path, include
from app.urls.UrlsHome.home import urlpatterns as urlHome
from app.urls.UrlsPublicar.publicar import urlpatterns as urlPublicar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urlHome)),
    path('publicar/',include(urlPublicar)),
]
