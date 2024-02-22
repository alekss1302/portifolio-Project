# portifolio/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from portifolio import views
from jobs.views import Home
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),  # Ensure 'blog.urls' is correct
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
