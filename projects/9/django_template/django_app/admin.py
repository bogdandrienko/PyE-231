from django.contrib import admin
from django_app import models

admin.site.site_header = "Панель управления"
admin.site.index_title = "Администрирование сайта"
admin.site.site_title = "Администрирование"

admin.site.register(models.Position)


class ContactAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели на панели администратора
    """

    list_display = ("username", "position", "number", "description", "is_completed", "created")
    list_display_links = ("username", "number")
    list_editable = ("is_completed",)
    search_fields = ["username", "number", "description"]
    list_filter = ("username", "position", "number", "description", "is_completed", "created")
    # filter_horizontal = ("tags",)  # M2M
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "username",
                    "position",
                    "number",
                    "description",
                )
            },
        ),
        (
            "Дополнительное",
            {"fields": ("is_completed", "created")},
        ),
    )


admin.site.register(models.Contact, ContactAdmin)
