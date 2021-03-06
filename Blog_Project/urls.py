from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Login_API.urls')),
    path('blog/', include('Blog_API.urls')),
    path('', views.index, name = 'index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
