from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Subject Name")
    description = models.TextField()

    def __str__(self):
        return self.name

    
class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.question 