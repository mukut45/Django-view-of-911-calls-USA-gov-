"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#from .views import top_zip_codes
from calls.views import top_zip_codes
from calls.views import home
from calls.views import top_townships
from calls.views import common_reason
from calls.views import ems_calls_by_day
from calls.views import max_fire_calls_month
from calls.views import traffic_calls_map

urlpatterns = [
    path('top-zip-codes/', top_zip_codes, name='top_zip_codes'), # This path is for top_zip_codes
    path('', home, name='home'), # This path is for home page
    path('top-townships/', top_townships, name='top-townships'), # This path is for top_townships
    path('common-reason/', common_reason, name='common-reason'), # This path is for common_reason
    path('ems-calls-by-day/', ems_calls_by_day, name='ems-calls-by-day'), # ems call url path
    path('max-fire-calls-month/', max_fire_calls_month, name='max-fire-calls-month'), # path for the months with most fire calls
    path('traffic-map/', traffic_calls_map, name='traffic-map'), # path for traffic webmap
    path('admin/', admin.site.urls),
]

