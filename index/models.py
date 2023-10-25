from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    name = models.CharField
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Token = models.CharField(max_length=50)


class Expense(models.Model):
    text = models.CharField(max_length=225)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.text, self.date, self.amount)


class Income (models.Model):
    text = models.CharField(max_length=225)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.text, self.date, self.amount)