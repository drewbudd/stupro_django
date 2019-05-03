"""stuprosample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserSerializer)
router.register(r'groups', views.GroupSerializer)
router.register(r'cadmodels', views.CADModelSerializer)
router.register(r'markers', views.MarkerSerializer)
router.register(r'statuses', views.StatusSerializer)
router.register(r'types', views.TypeSerializer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include(router.url))
]
