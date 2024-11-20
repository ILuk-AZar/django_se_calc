from django.db import models

# Create your models here.
from django.db import models

class Engine(models.Model):
    name = models.CharField(max_length=100)  # Название двигателя
    thrust = models.FloatField()  # Тяга двигателя в Ньютонах (единица силы)

    def __str__(self):
        return self.name  # Отображение названия двигателя в админке
from django.db import models
from django.contrib.auth.models import User

class CalculationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField()
    result = models.TextField()  # Результат вычислений в текстовом формате

class Env_settings(models.Model):
    gravity = models.FloatField()
    storage = models.IntegerField()

    def __str__(self):
        return self.name
