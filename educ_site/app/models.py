from django.db import models

class Learning(models.Model):
    name = models.CharField(max_length=255)
    content = models.FileField()
    grade_level = models.IntegerField()

    def __str__(self):
        return f"Grade {self.grade_level} :  {self.name}"
    
class Videos(models.Model):
    name = models.CharField(max_length=255)
    content = models.FileField()
    grade_level = models.IntegerField()

    def __str__(self):
        return f"Grade {self.grade_level} :  {self.name}"

class Activity(models.Model):
    name = models.CharField(max_length=255)
    content = models.FileField()
    grade_level = models.IntegerField()

    def __str__(self):
        return f"Grade {self.grade_level} :  {self.name}"
