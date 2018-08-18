from django.contrib import admin

from .models import News, Candidate, Query

admin.site.register(News)
admin.site.register(Candidate)
admin.site.register(Query)