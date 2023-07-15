
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDAI_ROOT)



