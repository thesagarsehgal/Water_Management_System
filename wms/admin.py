# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Plant,Tank,Plant_Data,Tank_Data

admin.site.register(Plant)
admin.site.register(Tank)
admin.site.register(Plant_Data)
admin.site.register(Tank_Data)