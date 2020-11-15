from .views import CompanyViewSet, EmployeeViewSet, PartnershipViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router_company = DefaultRouter()
router_company.register('company', CompanyViewSet, basename='companies')

router_emp = DefaultRouter()
router_emp.register('employees', EmployeeViewSet, basename='employees')

router_part = DefaultRouter()
router_part.register('partners', PartnershipViewSet, basename='partners')

urlpatterns = [
    path('api/', include(router_company.urls)),
    path('api/<int:pk>/', include(router_company.urls)),

    path('api/', include(router_emp.urls)),
    path('api/<int:pk>/', include(router_emp.urls)),

    path('api/', include(router_part.urls)),
    path('api/<int:pk>/', include(router_part.urls)),
]
