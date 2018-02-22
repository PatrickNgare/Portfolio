from django.contrib import admin
from .models import Tag,Portifolio


class PortifolioAdmin(admin.ModelAdmin):
    filter_horizontal=('porttags',)

# Register your models here.
admin.site.register(Tag)
admin.site.register(Portifolio,PortifolioAdmin)
