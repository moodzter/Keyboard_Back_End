from rest_framework import serializers 
from .models import Keyboard

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = ('id', 'brand', 'switches', 'keycaps', 'stabilizers', 'price', 'size',)