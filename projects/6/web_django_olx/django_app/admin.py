from django.contrib import admin
from django_app import models


# Register your models here.
admin.site.register(models.Item)
admin.site.register(models.CategoryItem)
admin.site.register(models.TagItem)
admin.site.register(models.Vip)
admin.site.register(models.CommentItem)
