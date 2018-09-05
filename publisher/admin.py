from django.contrib import admin
from publisher.models import InstagramAccount, Publication, Tag


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )


class PublicationAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "instagram_account_id", "publish_at")


class InstagramAccountAdmin(admin.ModelAdmin):
    list_display = ("username", "password")

admin.site.register(InstagramAccount, InstagramAccountAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Tag, TagAdmin)