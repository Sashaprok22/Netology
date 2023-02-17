from django.urls import path

from measurement.views import SensorsListCreateView, SensorRetrieveUpdateView, measurement_create_view

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path("sensors/", SensorsListCreateView.as_view(), name="sensors"),
    path("sensors/<int:pk>/", SensorRetrieveUpdateView.as_view(), name="sensor_update"),
    path("measurements/", measurement_create_view, name="measurements"),
]
