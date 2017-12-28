from django.conf.urls import url
from .views import DireccionApiView

urlpatterns = [
url(r'^$', DireccionApiView.as_view(), name="lista"),
url(r'^longitud/(?P<x>-\d*\.?\d+)/latitud/(?P<y>-\d*\.?\d+)/$', DireccionApiView.as_view(), name="coordenada"),
]