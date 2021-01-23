from django.contrib import admin
from basic_app.models import Movie,Audience

# Register your models here.

class MovieAdmin(admin.ModelAdmin):

    fields = ['length','title','release_year']

    search_fields = ['title','release_year']

    list_filter = ['release_year','length','title']

    list_display = ['title','length','release_year']

    list_editable = ['length']


class AudienceAdmin(admin.ModelAdmin):

    fields = ['contact','last_name','first_name']

    search_fields = ['first_name','last_name']

    list_filter = ['last_name','contact','first_name']

    list_display = ['first_name','last_name','contact']

    list_editable = ['contact']




admin.site.register(Movie,MovieAdmin)
admin.site.register(Audience,AudienceAdmin)
