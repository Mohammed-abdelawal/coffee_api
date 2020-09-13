from .models import CoffeeMachine, CoffeePod
from . import serializers
from rest_framework import mixins, viewsets
from django.db.models import Q

# Create your views here.


class CoffeeMachineViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin):
    serializer_class = serializers.CoffeeMachineSerializer
    queryset = CoffeeMachine.objects.all()

    def _params_to_strs(self, qs):
        """convert a list of string IDs to stringss list"""
        return [str(x) for x in qs.split(',')]

    def _params_to_ints(self, qs):
        """convert a list of string IDs to integers list"""
        l = []
        for x in qs.split(','):
            try:
                l.append(int(x))
            except ValueError:
                continue
        return l
    
    def get_queryset(self):
        """retrive the filtered Coffee Machines"""
        product_type_list = self.request.query_params.get('product_type')
        water_line_compatible = self.request.query_params.get('water_line_compatible')
        model_type_list = self.request.query_params.get('model_type')
        qs = self.queryset

        if product_type_list:
            product_type_ids = self._params_to_strs(product_type_list)
            qs = qs.filter(product_type__in=product_type_ids)
        if water_line_compatible :
            wlc = True if water_line_compatible.lower() in ['true', '1', 't', 'y', 'yes'] else False
            qs = qs.filter(water_line_compatible=wlc)

        if model_type_list:
            model_type_ids = self._params_to_ints(model_type_list)
            qs = qs.filter(model_type__in=model_type_ids)

        return qs


class CoffeePodViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    serializer_class = serializers.CoffeePodSerializer
    queryset = CoffeePod.objects.all()

    def _params_to_strs(self, qs):
        """convert a list of string IDs to stringss list"""
        return [str(x) for x in qs.split(',')]

    def _params_to_ints(self, qs):
        """convert a list of string IDs to integers list"""
        l = []
        for x in qs.split(','):
            try:
                l.append(int(x))
            except ValueError:
                continue
        return l
    
    def get_queryset(self):
        """retrive the filtered Coffee Pods"""
        product_type_list = self.request.query_params.get('product_type')
        coffee_flavor_list = self.request.query_params.get('coffee_flavor')
        pack_size_list = self.request.query_params.get('pack_size')
        qs = self.queryset

        if product_type_list:
            product_type_ids = self._params_to_strs(product_type_list)
            qs = qs.filter(product_type__in=product_type_ids)
        if coffee_flavor_list :
            coffee_flavor = self._params_to_ints(coffee_flavor_list)
            qs = qs.filter(coffee_flavor__in=coffee_flavor)

        if pack_size_list:
            pack_size = self._params_to_ints(pack_size_list)
            qs = qs.filter(pack_size__in=pack_size)

        return qs
