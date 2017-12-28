from rest_framework.generics import ListAPIView
from .serializers import DireccionSerializer
from ..models import Direccion

class DireccionApiView(ListAPIView):
    serializer_class = DireccionSerializer
    queryset = Direccion.objects.all()

    def get_queryset(self):
        x = self.kwargs.get('x')
        y = self.kwargs.get('y')
        query = "SELECT id, via, urbanizacion, distrito FROM seguimiento_point_georef(" + x + "," + y + ") AS (id integer, via varchar(60), urbanizacion varchar(60), distrito varchar(40));"

        if x is None or y is None:
            return Direccion.objects.all()
        else:
            return Direccion.objects.raw(query)