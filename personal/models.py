from django.db import models

# Create your models here.
class Tbcars(models.Model):
    carname = models.CharField(max_length=256, blank=False, null=False)
    carbrand = models.CharField(max_length=256, blank=False, null=False)
    carmodel = models.CharField(max_length=256, blank=False, null=False)
    carprice = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'tbcars'