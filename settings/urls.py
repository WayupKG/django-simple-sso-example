from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from settings.simple_sso import SSOClient

test_client = SSOClient(
    server_url=settings.SSO_SERVER,
    public_key=settings.SSO_PUBLIC_KEY,
    private_key=settings.SSO_PRIVATE_KEY,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include(test_client.get_urls())),
    path('', include('apps.core.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)),)
