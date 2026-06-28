from rest_framework import serializers
from stats.models.dieta import PlanAlimenticio

class PlanAlimenticioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanAlimenticio
        fields = '__all__'
        read_only_fields = ['id']