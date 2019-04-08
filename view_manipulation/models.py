from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=60)
    birthday = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name