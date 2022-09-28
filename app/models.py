from django.db import models

# Create your models here.

class Quiz(models.Model):
    text = models.TextField()
    answer1=models.TextField(null=True)
    answer2=models.TextField(null=True)
    correct_answer=models.IntegerField(default=1)
    # def __str__(self):
    #     return self.text