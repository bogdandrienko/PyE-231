from django.contrib import admin
from django_app import models

admin.site.site_header = "Панель управления"  # default: "Django Administration"
admin.site.index_title = "Администрирование сайта"  # default: "Site administration"
admin.site.site_title = "Администрирование"  # default: "Django site admin"


# Register your models here.


# РАСШИРЕННАЯ РЕГИСТРАЦИЯ МОДЕЛИ В АДМИНКЕ
class ItemAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели на панели администратора
    """

    list_display = ("author", "title", "description", "price", "category", "avatar", "file", "is_active", "is_moderate")
    list_display_links = ("author", "title")
    list_editable = ("is_active", "is_moderate")
    list_filter = ("author", "title", "description", "price", "category", "tags", "avatar", "file", "is_active", "is_moderate")
    filter_horizontal = ("tags",)
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "author",
                    "title",
                    "description",
                    "price",
                )
            },
        ),
        (
            "Дополнительное",
            {"fields": ("category", "tags", "avatar", "file", "is_active", "is_moderate")},
        ),
    )
    search_fields = ["title", "description"]


admin.site.register(models.Item, ItemAdmin)


admin.site.register(models.CategoryItem)
admin.site.register(models.TagItem)
admin.site.register(models.Vip)
admin.site.register(models.CommentItem)
admin.site.register(models.ItemRating)
admin.site.register(models.ItemBug)
admin.site.register(models.Room)
admin.site.register(models.Message)
admin.site.register(models.Profile)
admin.site.register(models.Action)
admin.site.register(models.GroupExtend)
