from django.db import models

class Category(models.Model):
    name        =   models.CharField(max_length=255, unique=True)

    def __str__(self, *args, **kwargs):
        return self.name
    
