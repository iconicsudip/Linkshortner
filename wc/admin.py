from django.contrib import admin
from wc.models import shorturl,notuserurl

# Register your models here.
admin.site.register(shorturl)
admin.site.register(notuserurl)