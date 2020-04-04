from django.db import models

# Create your models here.

class Person(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()
        
    return "%i : %s, %i years old, birth %s" % (self.id, self.name, self.age, self.birth)

