from django.contrib import admin

from .models import Species, Disposition, States, Taggers, TagTypes, LandLocation, TagPurchases, Tags # WHZoneCodes

class TaggersAdmin(admin.ModelAdmin):
    date_hierarchy = 'dateJoined'
    list_display = ('last', 'first', 'muni','st','phone','email')

class TagsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('tagno','date','species','location','tagger')
    search_fields = ['species__species']

admin.site.register(Species)
admin.site.register(Disposition)
admin.site.register(States)
admin.site.register(Taggers,TaggersAdmin)
admin.site.register(TagTypes)
admin.site.register(LandLocation)
admin.site.register(TagPurchases)
admin.site.register(Tags,TagsAdmin)

