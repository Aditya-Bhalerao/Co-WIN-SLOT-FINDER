"""vaccination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pincode/', views.PincodeView.as_view(),name='find_by_pin'),
    path('centers/<int:district_id>', views.CentersView.as_view(),name='centers'),
    path('', views.StatesView.as_view(),name='states'),
    path('districts/<int:state_id>', views.DistrictsView.as_view(),name='districts'),
    
]

urlpatterns += staticfiles_urlpatterns()