from django.contrib import admin
from herapp.models import People

# Register your models here.
class PeopleAdmin(admin.ModelAdmin):
    list_display=('name','address','department')
    list_editable=('address',)
    


admin.site.register(People,PeopleAdmin)