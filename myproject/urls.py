from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import home.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'),
    path('accounts/', include('reguser.urls')),
    path('', include('friends.urls')),
    path('', include('chat.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)