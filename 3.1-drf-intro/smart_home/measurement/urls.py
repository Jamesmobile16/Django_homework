from django.urls import path
from .views import SensorsView, SensorView, SensorDeleteView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurements/', SensorView.as_view()),
    path('sensor_delete/<id>/', SensorDeleteView.as_view())
]
