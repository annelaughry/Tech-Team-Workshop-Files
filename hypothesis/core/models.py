from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    
