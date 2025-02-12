from django.db import models

# Charging Request Model
class ChargingRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    bot_id = models.IntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default="pending")
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Charging Request by {self.user.username} - Status: {self.status}"