from rest_framework import serializers
from .models import CoffeePod, CoffeeMachine



class CoffeePodSerializer(serializers.ModelSerializer):
    """Serializer for Coffee Pods"""

    class Meta:
        model = CoffeePod
        fields = ('id', 'sku','get_product_type_display','coffee_flavor','pack_size')




class CoffeeMachineSerializer(serializers.ModelSerializer):
    """Serializer for Coffee Machines"""

    class Meta:
        model = CoffeeMachine
        fields = ('id', 'sku','product_type','water_line_compatible','model_type')

