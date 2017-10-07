from django.conf.urls import url,include
from . import views 
app_name="wms"

urlpatterns = [
	# 
    url(r'^$', views.index,name="index"),

    url(r'^getdata/$', views.get_data,name="getdata"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^login_prad/$', views.login_prad, name='login_prad'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # /about/
    url(r'^about/$', views.about,name="about"),
    url(r'^plants/$', views.plants,name="plants"),
    # /plant/123
    url(r'^plant/(?P<plant_id>[0-9]+)/$', views.plant_details,name="plant_details"),
    url(r'^plant/(?P<plant_id>[0-9]+)/data/$', views.plant_database,name="plant_database"),
    url(r'^construction/$', views.construction,name="construction"),
    
    # /plant/123
    # url(r'^tank/(?P<tank_id>[0-9]+)/$', views.tank_details,name="tank_details"),
]
