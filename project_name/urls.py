from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("project_name.core.urls", namespace="core")),
    path("admin/", admin.site.urls),
]
