from rest_framework import serializers

from api.models import ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
