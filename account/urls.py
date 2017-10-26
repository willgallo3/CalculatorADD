from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'createuser/$', views.createuser, name='createuser'),
   url(r'(?P<username>\w+)/$',views.profile_view,name='profile_view'),
   ]
