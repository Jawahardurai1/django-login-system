from rest_framework import viewsets
from .models import login
from .serializers import loginserializer
# from .serializers import registerserializer
from .models import login
class loginview(viewsets.ModelViewSet):
    queryset=login.objects.all()
    serializer_class=loginserializer
# class registerview(viewsets.ModelviewSet):
#     queryset=register.objects.all()
#     serializer_class=registerserializer