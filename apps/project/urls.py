from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.create, name='create'),
    url(r'^$', views.overview, name='overview'),
    url(r'^favorite/(?P<quote_id>\d+)/$', views.favorite, name='favorite'),
    url(r'^remove_favorite/(?P<quote_id>\d+)/$', views.remove_favorite, name='remove_favorite'),
    url(r'^user/(?P<user_id>\d+)/$', views.user_quotes, name='user_quotes')
]