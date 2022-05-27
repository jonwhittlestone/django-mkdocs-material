from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', admin.site.urls),
    url(r'^docs/', include('docs.urls'))
]
