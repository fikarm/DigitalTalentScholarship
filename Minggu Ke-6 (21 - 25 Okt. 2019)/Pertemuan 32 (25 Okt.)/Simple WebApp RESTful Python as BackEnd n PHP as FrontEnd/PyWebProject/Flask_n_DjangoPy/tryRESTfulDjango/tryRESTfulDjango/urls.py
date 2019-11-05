"""tryRESTfulDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from myapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    # siapkan parameter untuk ga
    path('', views.index),
    path('car', views.add_car),
    path('ga', views.run_ga),
    path('<str:car_name>', views.get_car),    
]


## jika dipublish di web online, gunakan script berikut:
#from django.contrib import admin
## from django.urls import path
#from django.conf.urls import url

#from myapp import views

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^$', views.index, name='home'),
#    url(r'^car/$', views.add_car, name='get_car_view'),
#    url(r'^ga/$', views.run_ga, name='run_ga_view'),
#    url(r'^<string>/$', views.get_car, name='get_car_view'),
#]

##urlpatterns = [
##    #path('admin/', admin.site.urls),
##    # siapkan parameter untuk ga
##    url('', views.index),
##    url('car', views.add_car),
##    url('ga', views.run_ga),
##    url('<str:car_name>', views.get_car),
##]


##from django.contrib import admin
##from django.conf.urls import url

##from myapp import views

##urlpatterns = [
##    #path('admin/', admin.site.urls),
##    # siapkan parameter untuk ga
##    url('', views.index),
##    # url('car', views.add_car),
##    # url(r'^search/$', views.search, name='search_view'),
##    url(r'^car', views.add_car, name='add_car_view'),
##    # url('ga', views.run_ga),
##    url(r'^ga', views.run_ga, name='run_ga_view'),
##    # url('', views.get_car,name='<str:car_name>'),
##    url(r'^$', views.get_car, name='get_car_view'),
##]