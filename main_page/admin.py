from django.contrib import admin
from . models import *


class AdvancesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Advances._meta.fields]

    class Meta:
        model = Advances


admin.site.register(Advances, AdvancesAdmin)


class RepliesImgInline(admin.TabularInline):
    model = RepliesImg
    extra = 0


class RepliesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Replies._meta.fields]
    inlines = [RepliesImgInline]

    class Meta:
        model = Replies


admin.site.register(Replies, RepliesAdmin)