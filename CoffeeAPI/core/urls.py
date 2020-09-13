from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('coffee-machines', views.CoffeeMachineViewSet)
router.register('coffee-pods', views.CoffeePodViewSet)

app_name = 'CoffeeFactoryApi'

urlpatterns = [
    path('', include(router.urls))
]
