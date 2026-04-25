from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from admins.web_views import root_router
from admins.web_views import sitemap_xml

urlpatterns = [
    path('', root_router, name='root_router'),
    path('admins/', include('admins.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)