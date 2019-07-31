from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.shortcuts import redirect
import profiles.urls
import accounts.urls
import employer.urls
import strategy.urls
import sales.urls
from . import views

# Personalized admin site settings like title and header
admin.site.site_title = "YesJob Site Admin"
admin.site.site_header = "YesJob Administration"

urlpatterns = [
    path("", lambda r: redirect('/strategy/status')),
    path("users/", include(profiles.urls)),
    path("admin/", admin.site.urls),
    path("accounts/", include(accounts.urls)),
    path("employer/", include(employer.urls)),
    path("strategy/", include(strategy.urls)),
    path("sales/", include(sales.urls)),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
