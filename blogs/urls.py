from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogs'
urlpatterns = [
    # post views
    path('', views.post_share, name='index'),
    path('404/', views.post_share1, name='404'),
    path('abhinav/', views.post_share2, name='abhinav'),
    # path('about/', views.post_share3, name='about'),
    path('bhavya/', views.post_share4, name='bhavya'),
    path('team/', views.post_share5, name='blog'),
    path('contact/', views.post_share6, name='contact'),
    path('gallery/', views.post_share7, name='gallery'),
    path('guneet/', views.post_share8, name='guneet'),

    path('kunal/', views.post_share10, name='kunal'),
    path('portfolio/', views.post_share11, name='portfolio'),
    path('tanishq/', views.post_share12, name='tanishq'),
    path('utkrisht/', views.post_share13, name='utkrisht'),
    path('about/', views.ResourceListView.as_view(),name='about'),
    path('resources/upload/', views.upload_resource,name='upload_resource'),
] 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)