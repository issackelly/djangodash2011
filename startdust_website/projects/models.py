from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)



