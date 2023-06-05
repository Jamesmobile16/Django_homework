from django.urls import path
from .views import SensorsView, SensorView, SensorDeleteView, MeasurementsAddView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensor/<id>/', SensorView.as_view()),
    path('add_measurements/', MeasurementsAddView.as_view()),
    path('sensor_delete/<id>/', SensorDeleteView.as_view())
]
