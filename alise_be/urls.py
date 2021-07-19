from django.contrib import admin
from django.urls import path, include
from user import urls as urls_user

urlpatterns = [
    path('user/', include(urls_user)),
    path('admin/', admin.site.urls),
]