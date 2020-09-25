from django.contrib import admin

from .models import *

admin.site.register(Question)
admin.site.register(Choice)
#admin.site.register(Zone)
admin.site.register(Place)
#admin.site.register(People)
admin.site.register(Person)
admin.site.register(importplace)