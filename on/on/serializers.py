from rest_framework import serializers
from .models import login 
class loginserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=login
        fields=('username','password')
    # class registerserializer(serializers.HyperlinkedModelSerializer):
    #     class Meta:
    #         model=register
    #         fields=('username','password','conform password','gmail')
