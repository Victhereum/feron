from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from feron.users.views import home_view

from feron.users.views import login_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", home_view, name="home"),
                  path('login/', login_view, name='login'),
                  # Django Admin, use {% url 'admin:index' %}
                  # User management
                  # path("users/", include("feron.users.urls", namespace="users")),
                  path("accounts/", include("allauth.urls")),
                  # Your stuff: custom urls includes go here
                  path('driver/', include('driver.url'), ),
                  path('investor/', include('investor.url'), ),
                  path('dashboard/', include('vehicle.url'), ),
                  # Third Parties
                  path('chaining/', include('smart_selects.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
