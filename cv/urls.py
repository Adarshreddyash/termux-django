from django.conf.urls import include, url

# This two if you want to enable the Django Admin: (recommended)
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # ... your url pat
    url(r'^works/', include('works.urls')),
]