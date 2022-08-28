# Imports
from django.contrib import admin
from django.urls import include, path

# Urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls'))
]
