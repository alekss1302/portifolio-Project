# portifolio/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
from portifolio import views
from jobs.views import home
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),  # Ensure 'blog.urls' is correct
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

