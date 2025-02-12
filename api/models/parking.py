from django.db import models
# Parking Spot Model

class ParkingSpot(models.Model):
    number = models.CharField(max_length=10, unique=True)
    is_reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Spot {self.number} - {'Reserved' if self.is_reserved else 'Available'}"