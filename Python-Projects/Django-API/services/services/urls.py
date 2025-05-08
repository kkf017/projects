from django.contrib import admin
from django.urls import path
 
from EnergyResource import views as EnergyResourceViews

urlpatterns = [
    path('', EnergyResourceViews.hello),
    path('new/', EnergyResourceViews.setEnergyResourceView),
    path('energy/', EnergyResourceViews.getEnergyResourceView),
    path('energy/search', EnergyResourceViews.getEnergyResourceSearchView),
    path('close', EnergyResourceViews.removeEnergyResourceView),
    path('admin/', admin.site.urls),
]
