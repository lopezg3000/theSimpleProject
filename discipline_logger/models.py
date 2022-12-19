from django.db import models


class Student(models.Model):
    first_name: models.CharField(max_length=255)
    last_name: models.CharField(max_length=255)


class Guardian(models.Model):
    first_name: models.CharField(max_length=255)
    last_name: models.CharField(max_length=255)
    email: models.EmailField(max_length=254)
    phone_number: models.CharField(max_length=12)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Offense(models.Model):
    date: models.DateTimeField('date of offense')
    offense_code: models.CharField(max_length=5)
    offense_description: models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Action(models.Model):
    action_code: models.CharField(max_length=5)
    action_description: models.CharField(max_length=255)
    offense = models.ForeignKey(Offense, on_delete=models.CASCADE)
