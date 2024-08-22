from django.db import models

# Create your models here.
class FaceEmbed(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    emotion = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"ID: {self.id}, Age: {self.age}, Emotion: {self.emotion}, Gender: {self.gender}, Timestamp: {self.timestamp}"