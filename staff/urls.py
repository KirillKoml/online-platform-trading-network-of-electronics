from django.urls import path

from staff.apps import StaffConfig
from staff.views import EmployeeListAPIView, EmployeeCreateAPIView, EmployeeUpdateAPIView, EmployeeDestroyAPIView, \
    EmployeeRetrieveAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = StaffConfig.name

urlpatterns = [
    # Урлы для модели сотрудников
    path('employee_list/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employee_create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('<int:pk>/employee_update/', EmployeeUpdateAPIView.as_view(), name='employee-update'),
    path('<int:pk>/employee_destroy/', EmployeeDestroyAPIView.as_view(), name='employee-destroy'),
    path('<int:pk>/employee_retrieve/', EmployeeRetrieveAPIView.as_view(), name='employee-list'),

    #
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]