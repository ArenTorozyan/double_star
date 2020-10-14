from django.contrib import admin
from . import models

# Register your models here.
# TabulaInLine allows ulitilizae the admin interface in django website with the ability to edit models on the same page as parent model.
class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
