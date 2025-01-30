"""
URL configuration for config project.

The `urlpatterns` list routes URLs to controllers. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function controllers
    1. Add an import:  from my_app import controllers
    2. Add a URL to urlpatterns:  path('', controllers.home, name='home')
Class-based controllers
    1. Add an import:  from other_app.controllers import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    path,
    include,
)
from main import controllers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('home/', controllers.home, name='home'),
    path('about/', controllers.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
