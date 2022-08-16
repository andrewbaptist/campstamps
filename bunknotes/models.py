from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name + "( $" + str(self.balance) + ")"


