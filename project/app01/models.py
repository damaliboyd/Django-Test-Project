from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Child(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
