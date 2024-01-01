from django.contrib import admin
from .models import Tag # , TaggedRecord, RelatedRecord

##########################################################################
""" General Models """
##########################################################################

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

# @admin.register(TaggedRecord)
# class TaggedRecordAdmin(admin.ModelAdmin):
#     pass

# @admin.register(RelatedRecord)
# class RelatedRecordAdmin(admin.ModelAdmin):
#     pass

##########################################################################
""" End File """
##########################################################################