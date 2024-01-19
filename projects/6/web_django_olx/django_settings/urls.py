from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    # prefix
    path("", include("django_app.urls")),
    # path("payment/", include("django_app.urls")),
]
