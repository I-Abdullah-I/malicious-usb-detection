from django.db import models

class Malware(models.Model):
    name = models.CharField(max_length=256)
    digest = models.TextField()
    whitelisted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
