# Imports
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# Urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls'))
]
# only runs in debug mode 
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
