"""hcims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
##from accounts import views as account_views
from accounts import urls as ac_url
from django.conf import settings
# from django.conf import settings
from django.conf.urls.static import static
from document_management import urls as dms_url
from crs import urls as crs_url

urlpatterns = [


    path('', include(dms_url)),

    path('', include(ac_url)),
    path('', include(crs_url)),

    # path('accounts/register/', account_views.register_view),
    # path('accounts/login/', account_views.login_view),
    # path('accounts/logout/', account_views.logout_view),


    path('admin/', admin.site.urls),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
