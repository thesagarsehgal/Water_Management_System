from django.conf.urls import url,include
from . import views 
app_name="wms"

urlpatterns = [
	# / ......... home page
    url(r'^$', views.index,name="index"),
    # /getdata/?pid=__&tid=__& .......takes data from the rasberry pi  and makes update in the database 
    url(r'^getdata/$', views.get_data,name="getdata"),
    # /register.............for a new  user registration
    url(r'^register/$', views.register, name='register'),
    # /login_user/ ........... for logging in  user
    url(r'^login_user/$', views.login_user, name='login_user'),
    # /logout_user/ ............. for logging out a user
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # /about/ ......... about us
    url(r'^about/$', views.about,name="about"),
    # /plants/ ........... list of all plants under a user
    url(r'^plants/$', views.plants,name="plants"),
    # /plant/13/ ....... views the plant details of the given plant id 
    url(r'^plant/(?P<plant_id>[0-9]+)/$', views.plant_details,name="plant_details"),
    # /plant/123/data/ ........... shows the current database of user
    url(r'^plant/(?P<plant_id>[0-9]+)/data/$', views.plant_database,name="plant_database"),
    # /under_construction/ .......... for pages not yet ready
    url(r'^under_construction/$', views.construction,name="construction"),
    # /add_plant/ ............for adding a new plant
    url(r'^add_plant/$',views.add_plant,name="add_plant"),
    # /add_tank/ ............ for adding a new Tank
    # url(r'^add_tank/$',views.add_tank,name="add_tank"),
    url(r'^plant/(?P<plant_id>[0-9]+)/change/$',views.change_location,name="change_location"),
]
