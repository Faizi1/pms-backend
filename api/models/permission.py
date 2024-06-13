from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=100)
    code_name = models.CharField(max_length=100, unique=True)
    module_name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
