from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from staff.models import Employee
from staff.serializers import EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    """Класс для вывода всех моделей сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateAPIView(CreateAPIView):
    """Класс для создания моделей сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        """Вмешиваюсь в логику контроллера для его правильной регистрации сотрудников."""
        # Сохраняю пользователя и сразу делаю его активным
        employee = serializer.save(is_active=True)

        # Хэширую пароль пользователя и сохраняю пользователя
        employee.set_password(employee.password)
        employee.save()


class EmployeeUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """Класс для детального просмотра модели сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer