from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("users.urls")),
    path("", include("orders.urls")),
    path("admin/", admin.site.urls),
]
