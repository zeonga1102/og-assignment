from django.contrib import admin
from .models import Status
from .models import Artist
from .models import Work


admin.site.register(Status)
admin.site.register(Artist)
admin.site.register(Work)