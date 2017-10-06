from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name="base"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('wms.urls')),
]
