from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name + "( $" + str(self.balance) + ")"

class Sender(models.Model):
    family = models.ForeignKey(Family,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.firstName + " " + self.lastName +" ("+self.family.name+") "

class Cabin(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Camper(models.Model):
    family = models.ForeignKey(Family,on_delete=models.CASCADE)
    cabin = models.ForeignKey(Cabin,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    def __str__(self):
        return self.firstName +" "+ self.lastName +" ("+self.family.name+") "+self.cabin.name

class tx(models.Model):
    date = models.DateField()
    sender = models.ForeignKey(Sender,on_delete=models.CASCADE)
    family = models.ForeignKey(Family,on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2,max_digits=10)


class Letter(models.Model):
    sender = models.ForeignKey(Sender,on_delete=models.CASCADE)
    camper = models.ForeignKey(Camper,on_delete=models.CASCADE)
    tx = models.ForeignKey(tx,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    isDelivered = models.BooleanField()
    date = models.DateField()
    def __str__(self):
        return self.title + " " +str(self.sender) + " "+str(self.camper)+ " "+self.date

class Photo():
   letter = models.ForeignKey(Letter,on_delete=models.CASCADE)
   data = models.URLField()
# TODO
#enrcypt passwords
