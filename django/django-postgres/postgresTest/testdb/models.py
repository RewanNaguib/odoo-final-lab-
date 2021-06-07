from django.db import models

class Rewan2(models.Model):
    id = models.BigIntegerField(primary_key="True")
    name = models.CharField(max_length=100,null="True",blank="True")
    description = models.CharField(max_length=300,null="True",blank="True")
    price = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)




