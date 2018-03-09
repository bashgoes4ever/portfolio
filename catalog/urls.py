from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^category/(?P<url_pretty>\w+)/$', views.category, name='category'),
    url(r'^catalog/(?P<url_pretty>\w+)/$', views.catalog, name='catalog'),
    url(r'^load_content/(?P<url_pretty>\w+)/', views.load_content, name='load_content'),
    url(r'^send_mail/', views.send_mail, name='send_mail')
]