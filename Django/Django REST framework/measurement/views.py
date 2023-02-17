# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorsListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

@api_view(["POST"])
def measurement_create_view(request):
    if not request.data.get("sensor") or not request.data.get("temperature"):
        return Response(status=400)
    sensor = Sensor.objects.get(id=request.data.get("sensor"))
    measurement = Measurement(sensor=sensor, temperature=request.data.get("temperature"))
    measurement.save()
    return Response(MeasurementSerializer(measurement).data, status=201)